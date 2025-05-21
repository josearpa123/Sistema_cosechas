import psycopg2
import random
import time
from datetime import date
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "cosechas"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def test_connection():
    try:
        conn = get_connection()
        conn.close()
        print("✅ Conexión a la base de datos exitosa.")
        return True
    except psycopg2.Error as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        return False

def insertar_tipos_cultivo_si_no_existen():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM tipocultivo;")
    count = cur.fetchone()[0]
    if count == 0:
        tipos = [("Café",), ("Caña de azúcar",)]
        cur.executemany("INSERT INTO tipocultivo (nombre_tipo) VALUES (%s);", tipos)
        conn.commit()
        print("✅ Tipos de cultivo insertados.")
    else:
        print("✅ Tipos de cultivo ya existen.")
    cur.close()
    conn.close()

def insertar_cultivos_si_no_existen():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM cultivo;")
    count = cur.fetchone()[0]
    
    if count == 0:
        # Obtener id de la primera finca disponible
        cur.execute("SELECT id_finca FROM finca LIMIT 1;")
        finca = cur.fetchone()
        if finca is None:
            print("❌ No hay fincas registradas. Registra una finca antes de insertar cultivos.")
            conn.close()
            return

        id_finca = finca[0]

        # Obtener tipos de cultivo
        cur.execute("SELECT id_tipocultivo FROM tipocultivo;")
        tipos = cur.fetchall()
        
        # Insertar un cultivo por tipo
        cultivos = [(tipo[0], id_finca) for tipo in tipos]
        cur.executemany("INSERT INTO cultivo (id_tipocultivo, id_finca) VALUES (%s, %s);", cultivos)
        conn.commit()
        print("✅ Cultivos insertados.")
    else:
        print("✅ Cultivos ya existen.")

    cur.close()
    conn.close()

def obtener_cultivos_por_tipo(nombre_tipo):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.id_cultivo
        FROM cultivo c
        JOIN tipocultivo tc ON c.id_tipocultivo = tc.id_tipocultivo
        WHERE tc.nombre_tipo = %s;
    """, (nombre_tipo,))
    cultivos = cur.fetchall()
    cur.close()
    conn.close()
    return [c[0] for c in cultivos]

def obtener_id_finca_por_nombre(nombre_finca):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id_finca FROM finca WHERE nombre = %s;", (nombre_finca,))
    resultado = cur.fetchone()
    cur.close()
    conn.close()
    return resultado[0] if resultado else None

def insertar_cosecha(id_cultivo, peso, precio):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO cosecha (fecha_cosecha, peso, precio, id_cultivo)
        VALUES (%s, %s, %s, %s);
    """, (date.today(), peso, precio, id_cultivo))
    conn.commit()
    cur.close()
    conn.close()

def simular_cosechas():
    nombre_finca = input("🏡 Ingresa el nombre de la finca para registrar cosechas: ")
    id_finca = obtener_id_finca_por_nombre(nombre_finca)
    
    if not id_finca:
        print(f"❌ No se encontró la finca con nombre '{nombre_finca}'.")
        return

    print(f"✅ Registrando cosechas para la finca '{nombre_finca}' (ID: {id_finca})")

    tipos = ["Café", "Caña de azúcar"]
    while True:
        for tipo in tipos:
            cultivos = obtener_cultivos_por_tipo(tipo)
            if not cultivos:
                print(f"⚠️ No se encontraron cultivos para el tipo '{tipo}'")
                continue
            for id_cultivo in cultivos:
                peso = round(random.uniform(100.0, 500.0), 2)
                precio = round(random.uniform(1.0, 5.0), 2)
                insertar_cosecha(id_cultivo, peso, precio)
                print(f"🌾 Insertada cosecha de {tipo} - Cultivo {id_cultivo} | Peso: {peso} kg | Precio: ${precio}")
        print("⏳ Esperando 10 segundos para la siguiente inserción...\n")
        time.sleep(10)

if __name__ == "__main__":
    if test_connection():
        insertar_tipos_cultivo_si_no_existen()
        insertar_cultivos_si_no_existen()
        simular_cosechas()
    else:
        print("No se puede iniciar la simulación por problemas de conexión.")
