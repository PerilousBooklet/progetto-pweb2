# Progetto di programmazione web 2

Progetto di programmazione web, parte 2.

## Setup

Create virtual environment:
  
`python -m venv virt_env`

Activate virtual environment:

`source virt_env/bin/activate`

Install django:

`python -m pip install Django`

Get the list of dependencies:

`pip freeze > requirements.txt`

Update `pip`:

`pip install --upgrade pip`

## Create project

`django-admin startproject project_name`

`python manage.py migrate`

## Create app

`python manage.py startapp app_name`

## Run project

`python manage.py runserver`

## Access webapp

App: `http://127.0.0.1:8000/app/`

Admin UI: `http://127.0.0.1:8000/admin/`

