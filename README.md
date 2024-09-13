# Progetto di Programmazione Web 2

## Indice

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
permettono di interfacciarsi con un database locale _PostgreSQL_ e interrogarlo.

Per creare l'interfaccia dell'applicazione web abbiamo utilizzato i template di Django.

Li abbiamo raggruppati nella cartella `templates`, abbinati alle rispettive views e collegati tra loro con gli url.

L'interazione con il database è gestita da Django tramite form e modali, gestite dai file `customlib.py`, `forms.py` e `views`.
Rispettivamente:
- `customlib.py` si occupa dell'interazione diretta con il database _Postgres_
- `forms.py` si occupa della generazione delle forms per permettergli di leggere input tramite Django.
- `views` si occupa di elaborare i templates per renderli dinamici.

I form sono utilizzati per cercare e inserire valori nei filtri e per svuotare i campi dei filtri stessi, 
mentre i modali sono utilizzati per modificare o rimuovere tuple nel database, tramite un menù popup dedicato.

## Setup Ambiente di Sviluppo

Le istruzioni riguardanti l'installazione e l'avvio del del server django e postgress si trovano nel pdf _Tutorial Windows_.

