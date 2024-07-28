# Progetto di programmazione web 2

Progetto di programmazione web, parte 2.

## Setup Database

`sudo -i`

`su postgres`

Initialize database:

`initdb --locale=C.UTF-8 --encoding=UTF8 -D /var/lib/postgres/data`

Start and enable `postgresql.service`:

`sudo systemctl start postgresql.service`

`sudo systemctl enable postgresql.service`

`sudo systemctl enable --now postgresql.service`

Add new db role/users (you must create 2 users: `pippo` and `user`, `pippo` should be your pc username)

`createuser --interactive`

Create new db:

`createdb pweb2`

Open DBeaver and do the following:

1. Database -> New Database Connection -> PostgreSQL
2. Write `pweb2` into the Server:Database field
3. Write `user` into the Authentication:Username field
4. In the top-left Database Navigator, expand the treeview until you reach `tables`
5. Double click on `tables`
6. In the second-from-top bar, click on the `SQL` button (to create a new SQL script)
7. Paste into it the contents of the `./sql/db_postgres_v2.sql` file
8. Run the script with `Alt + X`

## Setup Project

Create virtual environment:

`cd autostrade`

`python -m venv .venv`

Activate virtual environment:

`source .venv/bin/activate`

Install django:

`python -m pip install Django`

Get the list of dependencies:

`pip freeze > requirements.txt`

Update `pip`:

`pip install --upgrade pip`

## Create project

`django-admin startproject autostrade`

`python manage.py migrate`

## Create app

`python manage.py startapp app`

## Run project

`python manage.py runserver`

oppure usare `./run.sh` (richiede `tmux`)

## Access webapp

App: `http://127.0.0.1:8000/app/`

Admin UI: `http://127.0.0.1:8000/admin/`

