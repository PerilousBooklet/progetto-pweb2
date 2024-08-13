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
		cur.execute("select comune.codice, count(casello.codice) from comune join casello on comune.codice = casello.comune group by comune.codice, casello.codice order by casello.codice;")
		count_result = cur.fetchall()
		cur.execute("SELECT * FROM comune ORDER BY codice;")
	elif table == "autostrada":
		cur.execute("SELECT * FROM autostrada ORDER BY cod_naz;")
	else:
		cur.execute("SELECT * FROM casello ORDER BY codice;")
	
	result = cur.fetchall()

	for element in result:
		element = element + (0,)

	for i in range(len(result)):
		result[i] = result[i] + (0,)

	if "count_result" in locals():
		for i in range(len(result)):
			for j in range(len(count_result)-1):
				if result[i][0] == count_result[j][0]:
					temp_list = list(result[i])
					temp_list[len(temp_list)-1] = count_result[j][1]
					result[i] = tuple(temp_list)

	cur.close()
	conn.close()
	return result

def getDataListSearch(table: str, request):
	form_data = {}

	conn = createConnection()
	cur = conn.cursor()

	parsed_data = sqlGen(table, request)
	
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

def sqlGen(tabella: str, request):

	is_automatico_present = ""
	sql_finale = ""

	parsed_data = ()

	# Caso comune
	if tabella == "comune":
		if request.POST.get("codice") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + request.POST.get("codice") + "%",)

		if request.POST.get("provincia") == " " or request.POST.get("provincia") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + request.POST.get("provincia") + "%",)

		if request.POST.get("nome") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + request.POST.get("nome") + "%",)

		return parsed_data

	# Caso autostrada
	elif tabella == "autostrada":
		if request.POST.get("cod_naz") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + request.POST.get("cod_naz") + "%",)

		if request.POST.get("cod_eu") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + request.POST.get("cod_eu") + "%",)

		if request.POST.get("nome") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + request.POST.get("nome") + "%",)

		if request.POST.get("lunghezza") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + request.POST.get("lunghezza") + "%",)

		return parsed_data

	# Caso casello <- DA QUI
	else:
		sql_finale = "SELECT * FROM casello WHERE"

		if request.POST.get("codice") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + request.POST.get("codice") + "%",)
		
		if request.POST.get("cod_naz") == " ":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + request.POST.get("cod_naz") + "%",)

		if request.POST.get("comune") == " ":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + request.POST.get("comune") + "%",)

		if request.POST.get("nome") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + ("%" + request.POST.get("nome") + "%",)

		if request.POST.get("x") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + (request.POST.get("x"),)

		if request.POST.get("y") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + (request.POST.get("y"),)

		if request.POST.get("is_automatico") == "":
			parsed_data = parsed_data + ("%%",)
		else:
			print(request.POST.get("is_automatico").lower())
			if request.POST.get("is_automatico").lower() == "1":
				parsed_data = parsed_data + ("1",)
			elif request.POST.get("is_automatico").lower() == "0":
				parsed_data = parsed_data + ("0",)
			else:
				parsed_data = parsed_data + ("%%",)

		if request.POST.get("data_automazione") == "" or request.POST.get("data_automazione") is None:
			parsed_data = parsed_data + ("%%",)
		else:
			parsed_data = parsed_data + (request.POST.get("data_automazione"),)

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