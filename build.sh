#!/usr/bin/sh
clear
set -xe
python manage.py makemigrations
python manage.py migrate
python manage.py runserver