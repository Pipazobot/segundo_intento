#!/usr/bin/env bash

pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input
#arriba

python manage.py migrate

#despliegue 
#gunicorn segundo_intento.wsgi