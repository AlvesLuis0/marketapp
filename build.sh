#!/usr/bin/sh
clear
set -xe
python3 manage.py makemigrations
python3 manage.py migrate