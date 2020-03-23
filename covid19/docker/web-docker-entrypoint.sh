#!/bin/sh
set -e

echo foo

/bin/sh /app/docker/wait-for mysql:3306

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"
