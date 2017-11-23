#!/bin/bash
# -*- ENCODING: UTRF-8 -*-

echo Crear entorno virtual
virtualenv kernel

echo Cambiando a entorno virtual
source kernel/bin/activate

echo Instalando dependencias con pip
pip install -r requirements.txt

echo Listado de paquetes
pip list

echo Hacer migraciones
python manage.py makemigrations

echo Realizar migracion
python manage.py migrate

echo Iniciar servidor
python manage.py runserver
