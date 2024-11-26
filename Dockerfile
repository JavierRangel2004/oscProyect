# Dockerfile

# Imagen base de Python 3.9
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar y instalar dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . /app/

RUN apt-get update && apt-get install -y netcat-openbsd

# Copiar el entrypoint.sh
COPY entrypoint.sh /app/

# Dar permisos de ejecución al entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Exponer el puerto 8000
EXPOSE 8000

# Establecer el entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

# Comando por defecto para ejecutar el servidor de desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
