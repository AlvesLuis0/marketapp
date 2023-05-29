#!/usr/bin/sh
clear
set -xe
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username="admin" --email="admin@gmail.com"
python manage.py runserver