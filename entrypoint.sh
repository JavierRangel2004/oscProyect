#!/bin/bash

# Create necessary directories if they don't exist
mkdir -p data_import
mkdir -p data_export
mkdir -p media/organization_requests

# Wait until the database is available
echo "Waiting for PostgreSQL to be available..."
while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  sleep 0.1
done
echo "PostgreSQL is available"

# Apply migrations
echo "Applying migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser if it doesn't exist
echo "Creating superuser..."
python manage.py createsu

# Import data if JSON files exist in data_import
if ls data_import/*.json 1> /dev/null 2>&1; then
    echo "Importing data from JSON files in data_import..."
    for file in data_import/*.json; do
        echo "Importing data from $file..."
        python manage.py loaddata "$file"
    done
else
    echo "No JSON files found in data_import, skipping import."
fi

# Export data to data_export/data-<timestamp>.json
timestamp=$(date +"%Y%m%d%H%M%S")
export_file="data_export/data-${timestamp}.json"
echo "Exporting data to ${export_file}..."
python manage.py export_data ${export_file}

# Start the development server
echo "Starting the development server..."
exec "$@"
