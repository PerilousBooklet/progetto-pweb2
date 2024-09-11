from typing import Dict
import psycopg2

dbname = "pweb2"
username = "user"

def createConnection():
    conn = psycopg2.connect("dbname=" + dbname + " user=" + username)
    conn.set_session(autocommit=True)
    return conn

def getDataList(table: str):
    conn = createConnection()
    cur = conn.cursor()

    if table == "comune":
        cur.execute("SELECT comune.codice, comune.provincia, comune.nome, count(casello.codice) FROM comune left JOIN casello ON comune.codice = casello.comune GROUP BY comune.codice, comune.provincia, comune.nome ORDER BY comune.codice;")
        result = cur.fetchall()
    
    elif table == "autostrada":
        cur.execute("SELECT autostrada.cod_naz, autostrada.cod_eu, autostrada.nome, autostrada.lunghezza, count(casello.cod_naz) FROM autostrada JOIN casello ON autostrada.cod_naz = casello.cod_naz GROUP BY autostrada.cod_naz, autostrada.cod_eu, autostrada.nome, autostrada.lunghezza, casello.cod_naz ORDER BY casello.cod_naz;")
        result = cur.fetchall()
    
    else:
        cur.execute("SELECT casello.codice, casello.cod_naz, autostrada.nome, casello.comune, comune.nome, casello.nome, casello.x, casello.y, casello.is_automatico, casello.data_automazione FROM comune JOIN casello ON comune.codice = casello.comune JOIN autostrada ON autostrada.cod_naz = casello.cod_naz ORDER BY casello.codice;")
        result = cur.fetchall()

    cur.close()
    conn.close()
    return result

def getDataListSearch(table: str, post_data:dict[str, str]):
    form_data = {}

    conn = createConnection()
    cur = conn.cursor()

    parsed_data = sqlGen(table, post_data)
    
    if table == "comune":
        cur.execute("SELECT comune.codice, comune.provincia, comune.nome, count(casello.codice) FROM comune left JOIN casello ON comune.codice = casello.comune WHERE comune.codice LIKE %s AND comune.provincia LIKE %s AND comune.nome LIKE %s GROUP BY comune.codice, comune.provincia, comune.nome ORDER BY comune.codice;", parsed_data)
    elif table == "autostrada":
        print(parsed_data)
        cur.execute("SELECT autostrada.cod_naz, autostrada.cod_eu, autostrada.nome, autostrada.lunghezza, count(casello.cod_naz) FROM autostrada JOIN casello ON autostrada.cod_naz = casello.cod_naz WHERE autostrada.cod_naz LIKE %s AND autostrada.cod_eu LIKE %s AND autostrada.nome LIKE %s AND autostrada.lunghezza LIKE %s GROUP BY autostrada.cod_naz, autostrada.cod_eu, autostrada.nome, autostrada.lunghezza, casello.cod_naz ORDER BY casello.cod_naz;", parsed_data)
    else :
        cur.execute("SELECT casello.codice, casello.cod_naz, autostrada.nome, casello.comune, comune.nome, casello.nome, casello.x, casello.y, casello.is_automatico, casello.data_automazione FROM comune JOIN casello ON comune.codice = casello.comune JOIN autostrada ON autostrada.cod_naz = casello.cod_naz WHERE casello.codice LIKE %s AND casello.cod_naz LIKE %s AND casello.comune LIKE %s AND casello.nome LIKE %s AND casello.x LIKE %s AND casello.y LIKE %s AND CAST(casello.is_automatico AS TEXT) LIKE %s AND casello.data_automazione LIKE %s ORDER BY casello.codice;", parsed_data)
    result = cur.fetchall()
    

    cur.close()
    conn.close()
    return result

def addDataTable(table: str, request):

    parsed_data = (request.POST["codiceModalInsert"], request.POST["provinciaModalInsert"], request.POST["nomeModalInsert"])

    conn = createConnection()
    cur = conn.cursor()

    cur.execute("INSERT INTO comune (codice, provincia, nome) VALUES (%s, %s, %s);", parsed_data)

    
    cur.close()
    conn.close()
    return

def removeDataTable(table: str, request):

    parsed_data = (request.POST["codiceModalDelete"])

    conn = createConnection()
    cur = conn.cursor()

    cur.execute("DELETE FROM comune WHERE codice = '{0}';".format(parsed_data))
    
    cur.close()
    conn.close()
    return

def updateDataTable(table: str, request):

    parsed_data = (request.POST["provinciaModalEdit"], request.POST["nomeModalEdit"], request.POST["codiceModalEdit"])

    conn = createConnection()
    cur = conn.cursor()

    cur.execute("UPDATE comune SET provincia=%s, nome=%s WHERE codice=%s;", parsed_data)

    
    cur.close()
    conn.close()
    return

def sqlGen(tabella: str, post_data):

    is_automatico_present = ""
    sql_finale = ""

    parsed_data = ()

    # Caso comune
    if tabella == "comune":
        if post_data.get("codice") == "" or post_data.get("codice") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + (post_data.get("codice"),)

        if post_data.get("provincia") == " " or post_data.get("provincia") == "" or post_data.get("provincia") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + ("%" + post_data.get("provincia") + "%",)

        if post_data.get("nome") == "" or post_data.get("nome") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + ("%" + post_data.get("nome") + "%",)

        return parsed_data

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
            parsed_data = parsed_data + ("%" + post_data.get("lunghezza") + "%",)

        return parsed_data

    # Caso casello <- DA QUI
    else:
        sql_finale = "SELECT * FROM casello WHERE"

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

        if post_data.get("is_automatico") == "" or post_data.get("is_automatico") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            if post_data.get("is_automatico").lower() == "1":
                parsed_data = parsed_data + ("1",)
            elif post_data.get("is_automatico").lower() == "0":
                parsed_data = parsed_data + ("0",)
            else:
                parsed_data = parsed_data + ("%%",)

        if post_data.get("data_automazione") == "" or post_data.get("data_automazione") is None:
            parsed_data = parsed_data + ("%%",)
        else:
            parsed_data = parsed_data + (post_data.get("data_automazione"),)

        # Altrimenti se il valore di ricerca/inserimento contiene "'", darà errore
        return parsed_data

#
# Prende una lista di provincie uniche
#
def getProvincieUnique():
    listaelementi = getDataList("comune")
    listaUnica = [(" ", " ")]
    
    for elemento in listaelementi:
        if (elemento[1], elemento[1]) not in listaUnica:
            listaUnica.append((elemento[1], elemento[1]))
    return listaUnica

#
# Prende una lista di comuni unici
#
def getComuniUnique():
    listaelementi = getDataList("comune")
    listaUnica = [(" ", " ")]
    
    for elemento in listaelementi:
        if (elemento[0], elemento[0]) not in listaUnica:
            listaUnica.append((elemento[0], elemento[0]))
    return listaUnica

#
# Prende una lista di autostrade uniche
#
def getAutostradeUnique():
    listaelementi = getDataList("autostrada")
    listaUnica = [(" ", " ")]
    
    for elemento in listaelementi:
        if (elemento[0], elemento[0]) not in listaUnica:
            listaUnica.append((elemento[0], elemento[0]))
    return listaUnica

def insertToForm(post_data:Dict[str, str]):
    finalComune = {}
    
    finalComune["codice"] = post_data.get("codiceModalInsert")
    finalComune["provincia"] = post_data.get("provinciaModalInsert")
    finalComune["nome"] = post_data.get("nomeModalInsert")

    return finalComune