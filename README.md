# Progetto di programmazione web 2

Progetto di programmazione web, parte 2.

## Table of Contents

1. [Spiegazione delle scelte del progetto](#spiegazione-delle-scelte-del-progetto)
1. [Setup Database](#setup-database)
2. [Setup Django Project](#setup-django-project)
3. [Create Project](#create-project)
4. [Create Webapp](#create-webapp)
5. [Run Project](#run-project)
6. [Access Webapp](#access-webapp)

## Spiegazione delle scelte del progetto

In questo progetto abbiamo creato un'applicazione web che implementa le funzionalita' CRUD, 
utilizzando principalmente i framework `Django` e `Bootstrap`, come richiesto dalla consegna A, che 
permettono di interfacciarsi con un database locale PostgreSQL e interrogarlo.

L'applicazione fornisce un'interfaccia utente scritta in HTML e Bootstrap, contenuta nella cartella `templates`.

L'interazione con il database e' gestita da Django con ...

...

## Setup Database

`sudo -i`

`su postgres`

Inizializza il database:

`initdb --locale=C.UTF-8 --encoding=UTF8 -D /var/lib/postgres/data`

Avvia e abilita `postgresql.service`:

`sudo systemctl start postgresql.service`

`sudo systemctl enable postgresql.service`

`sudo systemctl enable --now postgresql.service`

Aggiungi nuovo database ruolo/utente (you must create 2 users: `pippo` and `user`, `pippo` should be your pc username)

`createuser --interactive`

Crea nuovo database:

`createdb pweb2`

Popola il database (you can use either the CLI way with `psql` or the GUI way with `DBeaver`):

usa:

```
cd ./progetto-pweb2/sql
psql database -f db_postgres_v2.sql
```

oppure:

Apri [DBeaver](https://dbeaver.io/):

1. Database -> New Database Connection -> PostgreSQL
2. Scrivi `pweb2` nel campo Server:Database
3. Scrivi `user` nel campo Authentication:Username
4. In alto a sinistra nel Database Navigator, espandi le viste fino a raggiungere `tables`
5. Doppio click su `tables`
6. Nella barra seconda-dall'alto, clicca sul bottone `SQL` per creare un nuovo script SQL
7. Incollaci il contenuto del file `./sql/db_postgres_v2.sql`
8. Avvia lo script con `Alt + X`

## Setup Django Project

Crea ambiente virtuale:

`cd autostrade`

`python -m venv .venv`

Avvia ambiente virtuale:

`source .venv/bin/activate`

Installa django:

`python -m pip install Django`

Ottieni la lista di dipendenze (serve solo la prima volta, adesso c'e' gia' il file `./autostrade/dependencies.txt`):

`pip freeze > requirements.txt`

Installa le dipendenze:

`pip install --requirement requirements.txt`

Aggiorna `pip`:

`pip install --upgrade pip`

## Create Project

`django-admin startproject autostrade`

`python manage.py migrate`

## Create App

`python manage.py startapp app`

## Run Project

`python manage.py runserver`

Oppure usare `./run.sh` (richiede `tmux`)

## Access Webapp

App: `http://127.0.0.1:8000/app/`

