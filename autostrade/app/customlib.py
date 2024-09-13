from typing import Dict
import psycopg2

# Dati per l'accesso al database
dbname = "pweb2"
username = "pweb2"
password = "pweb2"


# Crea la connessione verso il database
def createConnection():
    conn = psycopg2.connect(
        "dbname=" + dbname + " user=" + username + " password=" + password
    )
    conn.set_session(autocommit=True)
    return conn


# Prendi la tabella indicata in table e ritornala
def getDataList(table: str):
    conn = createConnection()
    cur = conn.cursor()

    # Caso tabella comune
    if table == "comune":
        cur.execute(
            "SELECT comune.codice, comune.provincia, comune.nome, count(casello.codice) FROM comune left JOIN casello ON comune.codice = casello.comune GROUP BY comune.codice, comune.provincia, comune.nome ORDER BY comune.codice;"
        )
        result = cur.fetchall()
    # Caso tabella autostrada
    elif table == "autostrada":
        cur.execute(
            "SELECT autostrada.cod_naz, autostrada.cod_eu, autostrada.nome, autostrada.lunghezza, count(casello.cod_naz) FROM autostrada JOIN casello ON autostrada.cod_naz = casello.cod_naz GROUP BY autostrada.cod_naz, autostrada.cod_eu, autostrada.nome, autostrada.lunghezza, casello.cod_naz ORDER BY casello.cod_naz;"
        )
        result = cur.fetchall()
    # Caso tabella casello
    else:
        cur.execute(
            "SELECT casello.codice, casello.cod_naz, autostrada.nome, casello.comune, comune.nome, casello.nome, casello.x, casello.y, casello.is_automatico, casello.data_automazione FROM comune JOIN casello ON comune.codice = casello.comune JOIN autostrada ON autostrada.cod_naz = casello.cod_naz ORDER BY casello.codice;"
        )
        result = cur.fetchall()

    # Chuidi la connessione e ritorna il risultato
    cur.close()
    conn.close()
    return result


# Prendi la tabella indicata in table e ritornala ma
# seguendo i parametri immessi dall'utente nella form
def getDataListSearch(table: str, post_data: dict[str, str]):
    form_data = {}

    conn = createConnection()
    cur = conn.cursor()

    # Crea la tupla contenente i dati inseriti dall'utente, essi
    # verranno messi automaticamente nella stringa della query, proteggendo
    # anche dalle sql injection
    parsed_data = sqlGen(table, post_data)

    # Caso tabella comune
    if table == "comune":
        cur.execute(
            "SELECT comune.codice, comune.provincia, comune.nome, count(casello.codice) FROM comune left JOIN casello ON comune.codice = casello.comune WHERE comune.codice LIKE %s AND comune.provincia LIKE %s AND comune.nome LIKE %s GROUP BY comune.codice, comune.provincia, comune.nome ORDER BY comune.codice;",
            parsed_data,
        )
    # Caso tabella autostrada
    elif table == "autostrada":
        print(parsed_data)
        cur.execute(
            "SELECT autostrada.cod_naz, autostrada.cod_eu, autostrada.nome, autostrada.lunghezza, count(casello.cod_naz) FROM autostrada JOIN casello ON autostrada.cod_naz = casello.cod_naz WHERE autostrada.cod_naz LIKE %s AND autostrada.cod_eu LIKE %s AND autostrada.nome LIKE %s AND autostrada.lunghezza LIKE %s GROUP BY autostrada.cod_naz, autostrada.cod_eu, autostrada.nome, autostrada.lunghezza, casello.cod_naz ORDER BY casello.cod_naz;",
            parsed_data,
        )
    # Caso tabella casello
    else:
        cur.execute(
            "SELECT casello.codice, casello.cod_naz, autostrada.nome, casello.comune, comune.nome, casello.nome, casello.x, casello.y, casello.is_automatico, casello.data_automazione FROM comune JOIN casello ON comune.codice = casello.comune JOIN autostrada ON autostrada.cod_naz = casello.cod_naz WHERE casello.codice LIKE %s AND casello.cod_naz LIKE %s AND casello.comune LIKE %s AND casello.nome LIKE %s AND casello.x LIKE %s AND casello.y LIKE %s AND CAST(casello.is_automatico AS TEXT) LIKE %s AND casello.data_automazione LIKE %s ORDER BY casello.codice;",
            parsed_data,
        )
    result = cur.fetchall()

    cur.close()
    conn.close()
    return result


# Aggiungi nuove righe
def addDataTable(table: str, request):
    # Faccio il parsing dei dati, rimuovendo
    # gli spazi prima del primo carattere e
    # dopo l'ultimo carattere
    parsed_data = (
        request.POST["codiceModalInsert"].strip(),
        request.POST["provinciaModalInsert"],
        request.POST["nomeModalInsert"].strip(),
    )

    conn = createConnection()
    cur = conn.cursor()

    # Esegue la query
    cur.execute(
        "INSERT INTO comune (codice, provincia, nome) VALUES (%s, %s, %s);", parsed_data
    )

    cur.close()
    conn.close()
    return


# Rimuovi le righe
def removeDataTable(table: str, request):

    # Fai il parsing dei dati
    parsed_data = request.POST["codiceModalDelete"]

    conn = createConnection()
    cur = conn.cursor()

    # Esegue la query
    cur.execute("DELETE FROM comune WHERE codice = '{0}';".format(parsed_data))

    cur.close()
    conn.close()
    return


# Rimuovi le righe
def updateDataTable(table: str, request):

    # Fai il parsing dei dati
    parsed_data = (
        request.POST["provinciaModalEdit"],
        request.POST["nomeModalEdit"],
        request.POST["codiceModalEdit"],
    )

    conn = createConnection()
    cur = conn.cursor()

    # Esegue la query
    cur.execute("UPDATE comune SET provincia=%s, nome=%s WHERE codice=%s;", parsed_data)

    cur.close()
    conn.close()
    return


# Qui viene creata la tupla che verrà dato alla funzione di
# ricerca in base alla tabella. nel caso le stringhe restutuite dalle
# form sono di lunghezza 0, o non hanno restituito il campo allora
# effettuerà una ricerca che accetta tutti i valori in quella colonna
# del database utilizzando l'operatore % con la comparazione LIKE
def sqlGen(tabella: str, post_data):

    # Inizzializzazione variabili di supporto
    parsed_data = ()

    # Caso comune
    if tabella == "comune":
        if post_data.get("codice") == "" or post_data.get("codice") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + (post_data.get("codice"),)

        if (
            post_data.get("provincia") == " "
            or post_data.get("provincia") == ""
            or post_data.get("provincia") is None
        ):
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + ("%" + post_data.get("provincia") + "%",)

        if post_data.get("nome") == "" or post_data.get("nome") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + ("%" + post_data.get("nome") + "%",)

    # Caso autostrada
    elif tabella == "autostrada":
        if post_data.get("cod_naz") == "" or post_data.get("cod_naz") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + (post_data.get("cod_naz"),)

        if post_data.get("cod_eu") == "" or post_data.get("cod_eu") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + ("%" + post_data.get("cod_eu") + "%",)

        if post_data.get("nome") == "" or post_data.get("nome") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + ("%" + post_data.get("nome") + "%",)

        if post_data.get("lunghezza") == "" or post_data.get("lunghezza") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + (post_data.get("lunghezza"),)

    # Caso casello
    else:
        if post_data.get("codice") == "" or post_data.get("codice") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + (post_data.get("codice"),)

        if post_data.get("cod_naz") == " " or post_data.get("cod_naz") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + (post_data.get("cod_naz"),)

        if post_data.get("comune") == " " or post_data.get("comune") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + ("%" + post_data.get("comune") + "%",)

        if post_data.get("nome") == "" or post_data.get("nome") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + ("%" + post_data.get("nome") + "%",)

        if post_data.get("x") == "" or post_data.get("x") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + (post_data.get("x"),)

        if post_data.get("y") == "" or post_data.get("y") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + (post_data.get("y"),)

        if (
            post_data.get("is_automatico") == ""
            or post_data.get("is_automatico") is None
        ):
            parsed_data = parsed_data + ("%%",)
        else:
            if post_data.get("is_automatico").lower() == "1":
                parsed_data = parsed_data + ("1",)
            elif post_data.get("is_automatico").lower() == "0":
                parsed_data = parsed_data + ("0",)
            else:
                parsed_data = parsed_data + ("%%",)

        if (
            post_data.get("data_automazione") == ""
            or post_data.get("data_automazione") is None
        ):
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + (post_data.get("data_automazione"),)

    # Ritorno la tupla di dati
    return parsed_data


# Prende una lista di provincie uniche
# Questa funzione derve per i menu di dropdown
def getProvincieUnique():
    listaelementi = getDataList("comune")
    # Valore vuoto per la ricerca senza
    # aver specificato la provincia
    listaUnica = [(" ", " ")]

    for elemento in listaelementi:
        if (elemento[1], elemento[1]) not in listaUnica:
            listaUnica.append((elemento[1], elemento[1]))
    return listaUnica


# Prende una lista di comuni unici
# Questa funzione derve per i menu di dropdown
def getComuniUnique():
    listaelementi = getDataList("comune")
    # Valore vuoto per la ricerca senza
    # aver specificato il comune
    listaUnica = [(" ", " ")]

    for elemento in listaelementi:
        if (elemento[0], elemento[0]) not in listaUnica:
            listaUnica.append((elemento[0], elemento[0]))
    return listaUnica


# Prende una lista di autostrade uniche
# Questa funzione derve per i menu di dropdown
def getAutostradeUnique():
    listaelementi = getDataList("autostrada")
    # Valore vuoto per la ricerca senza
    # aver specificato l'autostrada
    listaUnica = [(" ", " ")]

    for elemento in listaelementi:
        if (elemento[0], elemento[0]) not in listaUnica:
            listaUnica.append((elemento[0], elemento[0]))
    return listaUnica


# Questa funzione serve a convertire i dati del modale
# di inserimento in quello per la ricerca
def insertToForm(post_data: Dict[str, str]):
    finalComune = {}

    finalComune["codice"] = post_data.get("codiceModalInsert")
    finalComune["provincia"] = post_data.get("provinciaModalInsert")
    finalComune["nome"] = post_data.get("nomeModalInsert")

    return finalComune
