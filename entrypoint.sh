#!/bin/bash

# Esperar hasta que la base de datos esté disponible
echo "Esperando a que PostgreSQL esté disponible..."
while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  sleep 0.1
done
echo "PostgreSQL está disponible"

# Aplicar migraciones
echo "Aplicando migraciones..."
python manage.py makemigrations
python manage.py migrate

# Ejecutar el comando de importación de datos si existe
if [ -f "data_import/osc_web-db_2024-11-24.sql" ]; then
    echo "Importando datos desde osc_web-db_2024-11-24.sql..."
    python manage.py import_data data_import/osc_web-db_2024-11-24.sql
else
    echo "Archivo de importación de datos no encontrado, omitiendo importación."
fi

# Iniciar el servidor de desarrollo
echo "Iniciando el servidor de desarrollo..."
exec "$@"
