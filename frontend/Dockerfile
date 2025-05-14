# Usa Nginx como imagen base
FROM nginx:alpine

# Elimina el contenido por defecto de Nginx (opcional pero recomendable)
RUN rm -rf /usr/share/nginx/html/*

# Copia todo el contenido de src al directorio raíz de Nginx
COPY src/ /usr/share/nginx/html/

# Expón el puerto 80
EXPOSE 80
