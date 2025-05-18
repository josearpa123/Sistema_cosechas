import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def insertar_usuario(nombre_usuario, contrasena, nombre_rol):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT Id_Rol FROM Rol WHERE Nombre_Rol = %s;", (nombre_rol,))
    rol = cur.fetchone()
    if not rol:
        print(f"⚠️ Rol '{nombre_rol}' no existe.")
        cur.close()
        conn.close()
        return
    id_rol = rol[0]
    cur.execute("SELECT 1 FROM Usuario WHERE Nombre_Usuario = %s;", (nombre_usuario,))
    if cur.fetchone():
        print(f"⚠️ Usuario '{nombre_usuario}' ya existe.")
        cur.close()
        conn.close()
        return
    cur.execute("INSERT INTO Usuario (Nombre_Usuario, Contrasena, Id_Rol) VALUES (%s, %s, %s);",
                (nombre_usuario, contrasena, id_rol))
    conn.commit()
    print(f"✅ Usuario '{nombre_usuario}' insertado.")
    cur.close()
    conn.close()

def insertar_finca(nombre_finca, ubicacion=None, area_total=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM Finca WHERE Nombre = %s;", (nombre_finca,))
    if cur.fetchone():
        print(f"⚠️ La finca '{nombre_finca}' ya existe.")
        cur.close()
        conn.close()
        return
    cur.execute("INSERT INTO Finca (Nombre, Ubicacion, Area_Total) VALUES (%s, %s, %s);",
                (nombre_finca, ubicacion, area_total))
    conn.commit()
    print(f"✅ Finca '{nombre_finca}' insertada.")
    cur.close()
    conn.close()

def menu():
    while True:
        print("\n--- Menú de Inserción ---")
        print("1. Insertar usuario")
        print("2. Insertar finca")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            nombre = input("Nombre usuario: ")
            contrasena = input("Contraseña: ")
            rol = input("Rol (Administrador, Agricultor, Supervisor): ")
            insertar_usuario(nombre, contrasena, rol)
        elif opcion == "2":
            nombre = input("Nombre finca: ")
            ubicacion = input("Ubicación (opcional): ")
            area = input("Área total (opcional, numérico): ")
            area_val = float(area) if area else None
            insertar_finca(nombre, ubicacion if ubicacion else None, area_val)
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
