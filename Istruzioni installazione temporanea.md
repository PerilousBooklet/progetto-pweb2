# Istruzioni installazione
1. Installare WSL (Windows Subsystems for Linux).
2. Aggiorare Ubuntu `sudo apt-get update` `sudo apt-get upgrade`.
3. Installare Tmux `sudo apt install tmux`.
4. Installare Python `sudo apt install Python3`.
5. Installare Python3-venv `apt install python3.11-venv`.
6. Installare pip `sudo apt install pip`.
7. Copiare la cartella del progetto (progetto-pweb2) all'interno della home di WSL.
8. Entrare nella cartella `cd progetto-pweb2/autostrade`.
9. Eseguire `python3 -m venv .venv`.
12. Eseguire `source .venv/bin/activate`.
13. Eseguire `pip install -r requirements.txt`
14. Eseguire `pip install psycopg2-binary` in caso di errore.
12. Spostarsi poi nella directory _progetto-pweb2_ `con cd ..`.
13. Rendere eseguibili build.sh, run.shcon `chmod +x build.sh` e `chmod +x run.sh`.
14. Entrare in `cd autostrade/.venv/bin`.
15. Eseguire `chmod +x activate`.
16. tornare in _progetto-pweb2_ con `cd..`,  `cd..` e di nuovo `cd..`.
17. Eseguire _run.sh_ con `./run.sh`.




# nuovo tentativo
1. creare un utente chiamato `user` in Postgres.
2. creare un database di base qualsiasi (uguale al nome utente).
3. connettersi al database con il comando `psql -U user` o `psql -U user -d <nome_database>` per verificare che il database in questione esista.
4. creare un utente create user 'utente' with password '';

5. uscire dalla console facendo `\q`.
6. eseguire lo script sql `genera_database.sql` che si trova in `progetto-pweb2\sql\genera_database.sql`.

