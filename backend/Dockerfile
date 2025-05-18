# backend/Dockerfile

FROM python:3.11-slim

WORKDIR /app

# Copiamos solo requirements primero para aprovechar el cache de docker
COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código fuente
COPY src/ .

# Copiamos el archivo .env (debes tenerlo en backend/.env o cambiar ruta)
COPY ../src/.env .

CMD ["python", "generador.py"]
