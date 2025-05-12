# 🌱 Proyecto 6: Sistema de Gestión Agrícola (Café y Caña de Azúcar)

## 📘 Descripción General

Este proyecto consiste en el desarrollo de un sistema de gestión agrícola para el sector del café y la caña de azúcar. El objetivo principal es gestionar y proteger los datos de cosechas y ventas de manera segura, eficiente y automatizada, cumpliendo con requerimientos reales mediante historias de usuario implementadas con PostgreSQL, Docker, Python y prácticas de DevOps como respaldos automáticos y orquestación en red privada.

---

## 🧱 Tecnologías Utilizadas

- **PostgreSQL 16** – Sistema de base de datos relacional.
- **Python 3.10+** – Lógica de generación de datos y mantenimiento automatizado.
- **Docker** – Contenedores para la aplicación y base de datos.
- **Docker Compose** – Orquestación del entorno de desarrollo.
- **Kubernetes (opcional)** – Orquestación a nivel de clúster (para escalabilidad).
- **pg_basebackup** – Utilidad de PostgreSQL para respaldo físico.
- **Red privada Docker** – Aislamiento del entorno.

---

## 📁 Estructura del Proyecto

proyecto-agricola/
├── backend/
│ └── generator.py # Generador de cosechas aleatorias
├── db/
│ └── init.sql # Script SQL: tablas, roles y permisos
├── backups/
│ └── [respaldos semanales] # Carpeta montada para backups
├── scripts/
│ └── backup.sh # Script de respaldo con pg_basebackup
├── docker-compose.yml # Orquestación local de servicios
├── Dockerfile # Imagen de Python para el generador
├── k8s/
│ └── postgres-deployment.yaml # Configuración opcional para Kubernetes
├── README.md


---

## 🚀 Despliegue del Entorno (Docker Compose)

1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/proyecto-agricola.git
cd proyecto-agricola

    Inicia los servicios:

docker-compose up --build

    Accede a los contenedores:

    PostgreSQL disponible en: localhost:5432

    Usuario por defecto: admin

    Contraseña: admin

    Base de datos: agricola_db

👥 Roles y Accesos

Se crean dos roles principales:

    gerente_finca: acceso total a las tablas cosechas y ventas.

    trabajador_campo: acceso solo a sus registros mediante vistas con restricciones.

📌 Historias de Usuario Implementadas
1. 📦 Respaldo Semanal Automático

    Script backup.sh utiliza pg_basebackup para generar una copia completa semanal.

    Respaldos almacenados en el volumen backups/.

2. 🔐 Control de Accesos

    Roles configurados en SQL (init.sql) con permisos específicos según el tipo de usuario.

3. 📊 Reportes de Producción

    Consulta para obtener toneladas cosechadas por finca y tipo de cultivo:

SELECT ubicacion, producto, SUM(cantidad) as total_kg
FROM cosechas
GROUP BY ubicacion, producto;

4. 🧪 Optimización de Índices

    Índices creados para producto, ubicacion, y fecha para acelerar consultas frecuentes.

5. 🛠️ Mantenimiento Preventivo

    Transacciones SQL periódicas para validación y actualización segura de datos.

6. 🔒 Seguridad de Datos

    Soporte para cifrado en tránsito (mediante configuración de PostgreSQL con SSL).

    Posible cifrado en columnas sensibles usando pgcrypto.

7. 🔄 Generación Aleatoria de Cosechas

    Script en Python (generator.py) que simula nuevos registros aleatorios mediante hilos de ejecución.

🧪 Scripts Clave
🔁 generator.py

Simula registros con productos, cantidades y precios aleatorios.
Se ejecuta constantemente insertando datos simulados.
💾 backup.sh

Script bash automatizado que se puede ejecutar desde cron o manualmente:

docker exec db pg_basebackup -U postgres -D /backups -F tar -z -P

🧰 Comandos Útiles

    Ingresar al contenedor PostgreSQL:

docker exec -it db psql -U postgres

    Ejecutar respaldo manual:

bash scripts/backup.sh

    Ver registros generados:

docker logs generator

☸️ Despliegue en Kubernetes (opcional)

Puedes usar los manifiestos YAML del directorio k8s/:

kubectl apply -f k8s/postgres-deployment.yaml

✅ Requisitos

    Docker 20.10+

    Docker Compose 1.29+

    Python 3.10 (si corres scripts fuera del contenedor)

    (Opcional) Kubernetes con kubectl configurado

📜 Licencia

Este proyecto es de uso académico y educativo. No está destinado a producción sin pruebas adicionales.


---

Este `README.md` te da una **documentación profesional y completa** que puedes subir a GitHub o entregar directamente. Si deseas, puedo generarte ahora los archivos correspondientes: `init.sql`, `docker-compose.yml`, `generator.py` y `backup.sh`. ¿Quieres que te los dé ahora?
