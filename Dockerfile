# Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Instalar netcat y dos2unix
RUN apt-get update && apt-get install -y netcat-openbsd dos2unix

# Copiar todo el código
COPY . /app/

# Convertir line endings y establecer permisos
RUN dos2unix /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
