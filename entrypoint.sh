#!/bin/bash

# Crear directorios de importación y exportación si no existen
mkdir -p data_import
mkdir -p data_export

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

# Crear superusuario si no existe
echo "Creando superusuario..."
python manage.py createsu

# Ejecutar el comando de importación de datos si existe un archivo JSON en data_import
if ls data_import/*.json 1> /dev/null 2>&1; then
    echo "Importando datos desde archivos JSON en data_import..."
    for file in data_import/*.json; do
        echo "Importando datos desde $file..."
        python manage.py loaddata "$file"
    done
else
    echo "No se encontraron archivos JSON en data_import, omitiendo importación."
fi

# Exportar datos a data_export/data-<timestamp>.json
timestamp=$(date +"%Y%m%d%H%M%S")
export_file="data_export/data-${timestamp}.json"
echo "Exportando datos a ${export_file}..."
python manage.py export_data ${export_file}

# Iniciar el servidor de desarrollo
echo "Iniciando el servidor de desarrollo..."
exec "$@"

