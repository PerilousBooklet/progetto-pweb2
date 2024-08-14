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
		cur.execute("select comune.codice, comune.provincia, comune.nome, count(casello.codice) from comune left join casello on comune.codice = casello.comune group by comune.codice, comune.provincia, comune.nome order by comune.codice;")
		result = cur.fetchall()
	
	elif table == "autostrada":
		cur.execute("select autostrada.cod_naz, autostrada.cod_eu, autostrada.nome, autostrada.lunghezza, count(casello.cod_naz) from autostrada join casello on autostrada.cod_naz = casello.cod_naz group by autostrada.cod_naz, autostrada.cod_eu, autostrada.nome, autostrada.lunghezza, casello.cod_naz order by casello.cod_naz;")
		result = cur.fetchall()
	
	else:
		cur.execute("SELECT casello.codice, casello.cod_naz, casello.comune, casello.nome, casello.x, casello.y, casello.is_automatico, casello.data_automazione, comune.nome, autostrada.nome FROM comune JOIN casello ON comune.codice = casello.comune JOIN autostrada ON autostrada.cod_naz = casello.cod_naz ORDER BY casello.codice;")
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
		cur.execute("SELECT * FROM comune WHERE codice LIKE %s AND provincia LIKE %s AND nome LIKE %s ORDER BY codice;", parsed_data)
	elif table == "autostrada":
		cur.execute("SELECT * FROM autostrada WHERE cod_naz LIKE %s AND cod_eu LIKE %s AND nome LIKE %s AND lunghezza LIKE %s ORDER BY cod_naz;", parsed_data)
	else :
		cur.execute("SELECT * FROM casello WHERE codice LIKE %s AND cod_naz LIKE %s AND comune LIKE %s AND nome LIKE %s AND x LIKE %s AND y LIKE %s AND CAST(is_automatico AS TEXT) LIKE %s AND data_automazione LIKE %s ORDER BY codice;", parsed_data)
	result = cur.fetchall()
	

	cur.close()
	conn.close()
	return result

def addDataTable(table: str, request):

	parsed_data = (request.POST["codice"], request.POST["provincia"], request.POST["nome"])

	conn = createConnection()
	cur = conn.cursor()

	cur.execute("INSERT INTO comune (codice, provincia, nome) VALUES (%s, %s, %s);", parsed_data)

	
	cur.close()
	conn.close()
	return

def removeDataTable(table: str, request):

	parsed_data = (request.POST["codiceModal"])

	conn = createConnection()
	cur = conn.cursor()

	cur.execute("DELETE FROM comune WHERE codice = %s;", parsed_data)
	
	cur.close()
	conn.close()
	return

def updateDataTable(table: str, request):

	parsed_data = (request.POST["provinciaModal"], request.POST["nomeModal"], request.POST["codiceModal"])

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
		if post_data.get("codice") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + post_data.get("codice") + "%",)

		if post_data.get("provincia") == " " or post_data.get("provincia") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + post_data.get("provincia") + "%",)

		if post_data.get("nome") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + post_data.get("nome") + "%",)

		return parsed_data

	# Caso autostrada
	elif tabella == "autostrada":
		if post_data.get("cod_naz") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + post_data.get("cod_naz") + "%",)

		if post_data.get("cod_eu") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + post_data.get("cod_eu") + "%",)

		if post_data.get("nome") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + post_data.get("nome") + "%",)

		if post_data.get("lunghezza") == "":
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
			parsed_data = parsed_data + ("%" + post_data.get("codice") + "%",)
		
		if post_data.get("cod_naz") == " " or post_data.get("cod_naz") is None:
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + post_data.get("cod_naz") + "%",)

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