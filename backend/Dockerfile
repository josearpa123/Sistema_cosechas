# Imagen base con Python
FROM python:3.11-slim

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar requirements y código fuente
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer el puerto si usas algún servicio HTTP (opcional)
# EXPOSE 8000

# Comando por defecto: ejecutar el archivo principal
CMD ["python", "src/main.py"]
