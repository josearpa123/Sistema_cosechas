# Proyecto 6: Sistema de Gestión Agrícola (Café y Caña de Azúcar)

## 🧱 Descripción General

Este proyecto consiste en un sistema de gestión agrícola para cultivos de café y caña de azúcar. Incluye generación automática de datos de cosechas, reportes de producción, control de acceso mediante roles, respaldo automatizado de la base de datos y otras tareas de mantenimiento.

El sistema se implementa usando:

- PostgreSQL como base de datos.
- Python (ó Java) para lógica de negocio y generación de datos.
- Docker y Docker Compose para contenerización.
- Kubernetes (opcionalmente) para orquestación.
- Red privada para aislamiento del entorno.
- Seguridad en tránsito y en reposo para datos sensibles.

---

## 🛠️ Tecnologías

- **PostgreSQL 16+**
- **Python 3.10+** o **Java 17**
- **Docker**
- **Docker Compose**
- **Kubernetes (opcional para despliegue en clúster)**
- **pg_basebackup** para respaldo

---

## 📦 Estructura del Proyecto

agro-data-system/
├── backend/
│ └── generator.py # Generador de datos aleatorios (Python)
├── db/
│ └── init.sql # Script para roles, tablas y permisos
├── backups/
│ └── [auto-generated] # Carpeta donde se almacenan los backups
├── docker-compose.yml
├── Dockerfile (opcional)
├── k8s/ # Archivos de Kubernetes (si se implementa)
│ └── postgres-deployment.yaml
├── README.md


---

## 🚀 Instrucciones de Despliegue (Docker Compose)

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/proyecto-agricola.git
   cd proyecto-agricola

    Construye e inicia los servicios:

    docker-compose up --build

    El sistema desplegará:

        Una base de datos PostgreSQL inicializada con roles y permisos.

        Un generador automático de registros de cosecha.

    Acceso a la base de datos:

        Host: localhost

        Puerto: 5432

        Usuario: admin

        Password: admin

🧩 Historias de Usuario Implementadas
Historia 1: Respaldo Semanal

    Script backup.sh usa pg_basebackup para generar copias semanales de la base de datos.

Historia 2: Control de Acceso

    Roles:

        gerente_finca: acceso completo a cosechas y ventas.

        trabajador_campo: acceso solo a sus actividades.

    Implementado vía SQL en init.sql.

Historia 3: Reportes de Producción

    Consultas agregadas por finca y tipo de cultivo (GROUP BY finca, producto).

Historia 4: Optimización de Índices

    Índices creados sobre columnas consultadas frecuentemente: producto, ubicacion, fecha.

Historia 5: Mantenimiento Preventivo

    Uso de transacciones para actualizar tablas de cultivos de forma segura.

Historia 6: Seguridad de Datos

    Cifrado en tránsito (SSL en PostgreSQL)

    Posible cifrado en reposo mediante columnas encriptadas.

Historia 7: Generación Automática

    Script generator.py simula nuevas cosechas en intervalos aleatorios con uso de hilos.

🧪 Pruebas

    Pruebas de inserción automática y respaldo pueden verificarse mediante logs:

    docker logs generator
    docker exec -it db pg_basebackup -U postgres -D /var/lib/postgresql/backups

⚙️ Kubernetes (opcional)

Si deseas escalar o simular un entorno real:

kubectl apply -f k8s/postgres-deployment.yaml

📌 Notas

    Se recomienda montar volúmenes persistentes para la base de datos y backups.

    El generador de cosechas puede adaptarse a Java si se prefiere.

    El proyecto cumple con las buenas prácticas de contenedores y separación de servicios.

✍️ Autor

Tu Nombre - Estudiante de Ingeniería de Sistemas
Curso: Gestión de Bases de Datos
Profesor: [Nombre del profesor]
Universidad: [Nombre de tu universidad]


---

¿Te gustaría que te dé los archivos `docker-compose.yml`, `init.sql`, y `generator.py` como siguiente paso?

Dijiste:
Listo ahora dame todo lo que hiria en el readme
ChatGPT dijo:

Perfecto, a continuación te entrego todo el contenido completo y detallado que debe ir en tu README.md, incluyendo introducción, tecnologías, despliegue, historias de usuario desarrolladas, uso del sistema, scripts y créditos.

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
