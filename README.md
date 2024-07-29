# Progetto di programmazione web 2

Progetto di programmazione web, parte 2.

## Table of Contents

1. [Spiegazione delle scelte del progetto](#spiegazione-delle-scelte-del-progetto)
2. [Setup Ambiente di Sviluppo](#setup-ambiente-di-sviluppo)
3. [Setup Database](#setup-database)
4. [Setup Django Project](#setup-django-project)
5. [Create Project](#create-project)
6. [Create Webapp](#create-webapp)
7. [Run Project](#run-project)
8. [Access Webapp](#access-webapp)

## Spiegazione delle scelte del progetto

In questo progetto abbiamo creato un'applicazione web che implementa le funzionalita' CRUD, 
utilizzando principalmente i framework `Django` e `Bootstrap`, come richiesto dalla consegna A, che 
permettono di interfacciarsi con un database locale PostgreSQL e interrogarlo.

Per creare l'interfaccia dell'applicazione web abbiamo utilizzato i template di Django.

Li abbiamo raggruppati nella cartella `templates`, abbinati alle rispettive views e collegati tra loro con gli url.

L'interazione con il database e' gestita da Django tramite form e modali.

I form sono utilizzati per cercare e inserire valori nei filtri e per svuotare i campi dei filtri stessi, 
mentre i modali sono utilizzati per modificare o rimuovere tuple nel database, tramite un menu popup dedicato.

## Setup Ambiente di Sviluppo

<!-- TODO: sostituire la guida per VM con la guida per Windows -->

Premessa:
1. le seguenti istruzioni potrebbero sembrare lunghe, ma questo sistema e' l'unico che funzioni su ogni sistema operativo.
2. Dopo aver constatato che la preparazione del progetto su Windows nativamente e con WSL2 non era possibile, abbiamo scritto la procedura per le macchine virtuali.

Utilizzare una macchina virtuale con [Virtualbox](https://www.virtualbox.org/);

Installare il sistema operativo [EndeavourOS](https://mirror.alpix.eu/endeavouros/iso/EndeavourOS_Endeavour-2024.06.25.iso), uns distribuzione linux semplice e user-friendly.

Quando il sistema operativo e' installato, riavviare ed effettuare il login.

A questo punto, installare le dipendenze: 

Aprire il terminale e avviare i seguenti comandi:

```sh
sudo pacman -Syu python python-virtualenv postgresql tmux
```

## Setup Database

Aprire il terminale.

Scrivere i seguenti comandi per elevare i privilegi esecutivi:

`sudo -i`

`su postgres`

Inizializza il database:

`initdb --locale=C.UTF-8 --encoding=UTF8 -D /var/lib/postgres/data`

Avvia e abilita `postgresql.service`:

`sudo systemctl enable --now postgresql.service`

Aggiungi nuovo database ruolo/utente (bisogna usare 2 utenti: `pippo` and `user`, `pippo` e' il nome utente)

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

