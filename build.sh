#!/usr/bin/bash
source virt_env/bin/activate
cd ./autostrade || exit
python manage.py runserver
