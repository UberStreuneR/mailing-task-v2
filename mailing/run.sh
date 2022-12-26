#!/bin/bash

[ -z $DB_HOST ] && DB_HOST="db"
[ -z $DB_PORT ] && DB_PORT="5432"

echo "Waiting for PostgreSQL..."
while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done
echo "PostgreSQL started"

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000