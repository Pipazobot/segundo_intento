#!/usr/bin/env bash

pip install -r requirements.txt

python manage.py migrate

#despliegue 
#gunicorn segundo_intento.wsgi