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

# Exponer el puerto 8000
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
