#!/usr/bin/sh
clear
set -xe
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser --username="admin" --email="admin@gmail.com"
python3 manage.py runserver