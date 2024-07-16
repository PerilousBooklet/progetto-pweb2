#!/usr/bin/bash
source autostrade/.venv/bin/activate
cd ./autostrade || exit
python manage.py runserver
