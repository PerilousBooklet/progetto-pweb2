from genericpath import exists
from typing import Any
from unittest import result
from django.http import HttpRequest
import psycopg2

dbname = "pweb2"
username = "user"

def createConnection():
	conn = psycopg2.connect("dbname=" + dbname + " user=" + username)
	return conn

def getDataList(table: str) -> list[tuple]:
	conn = createConnection()
	cur = conn.cursor()
	
	cur.execute("SELECT * FROM {0};".format(table))
	result = cur.fetchall()
	conn.commit()

	cur.close()
	conn.close()
	return result

def getDataListSearch(table: str, request) -> list[tuple]:
	form_data = {}
	form_data["tabella"] = table

	conn = createConnection()
	cur = conn.cursor()

	sql = sqlGen(form_data, request)

	print("SQL -> " + sql)
	
	cur.execute(sql)
	result = cur.fetchall()
	conn.commit()

	cur.close()
	conn.close()
	return result

def addDataTable(table: str, request):
	table = "comune"
	conn = createConnection()
	cur = conn.cursor()

	if table == "autostrada":
		cur.execute("INSERT INTO autostrada (cod_naz, cod_eu, nome, lunghezza) VALUES ('{cod_naz}', '{cod_eu}', '{nome}', '{lunghezza}');".format(**data))
	elif table == "comune": 
		cur.execute("INSERT INTO comune (codice, provincia, nome) VALUES ('{codice}', '{provincia}', '{nome}');".format(**request.POST).replace("['", "").replace("']", ""))
	else:
		cur.execute("INSERT INTO casello (codice, cod_naz, comune, nome, x, y, is_automatico, data_automazione) VALUES ('{codice}', '{cod_naz}', '{comune}', '{nome}', '{x}', '{y}', '{is_automatico}', '{data_automazione}');".format(**data))

	conn.commit()
	cur.close()
	conn.close()
	return

def removeDataTable(table: str, request):
	table = "comune"
	conn = createConnection()
	cur = conn.cursor()

	if table == "autostrada":
		cur.execute("DELETE FROM autostrada WHERE cod_naz = '{cod_naz}';".format(**data))
	elif table == "comune": 
		cur.execute("DELETE FROM comune WHERE codice = '{codiceModal}';".format(**request.POST).replace("['", "").replace("']", ""))
	else:
		cur.execute("DELETE FROM casello WHERE codice = '{codice}' AND cod_naz = '{cod_naz}' AND comune = '{comune}';".format(**data))

	conn.commit()
	cur.close()
	conn.close()
	return

def updateDataTable(table: str, request):
	table="comune"
	conn = createConnection()
	cur = conn.cursor()

	if table == "autostrada":
		cur.execute("UPDATE autostrada SET cod_eu='{cod_eu}', nome='{nome}', lunghezza={lunghezza} WHERE cod_naz='{cod_naz}';".format(**data))
	elif table == "comune":
		cur.execute("UPDATE comune SET provincia='{provinciaModal}', nome='{nomeModal}' WHERE codice='{codiceModal}';".format(**request.POST).replace("['", "").replace("']", ""))
	else:
		# RICODA DI CONTROLLARE LA COSA DELLA DATA
		if data.get("data_automazione") == None:
			cur.execute("UPDATE casello SET cod_naz='{cod_naz}', comune='{comune}', nome='{nome}', x='{x}', y='{y}', is_automatico={is_automatico}, data_automazione=NULL WHERE codice='{codice}' AND cod_naz='{cod_naz}' AND comune='{comune};".format(**data))
		else:
			cur.execute("UPDATE casello SET cod_naz='{cod_naz}', comune='{comune}', nome='{nome}', x='{x}', y='{y}', is_automatico={is_automatico}, data_automazione={data_automazione} WHERE codice='{codice}' AND cod_naz='{cod_naz}' AND comune='{comune};".format(**data))

	conn.commit()
	cur.close()
	conn.close()
	return

def sqlGen(form_data: dict, request) -> str:

	is_automatico_present = ""
	sql_finale = ""

	# Caso comune
	if form_data.get("tabella") == "comune":
		if request.POST.get("codice") == "":
			form_data["codice"] = "%%"
		else:
			form_data["codice"] = "%" + request.POST.get("codice") + "%"

		if request.POST.get("provincia") == " " or request.POST.get("provincia") == "":
			form_data["provincia"] = "%%"
		else:
			form_data["provincia"] = "%" + request.POST.get("provincia") + "%"

		if request.POST.get("nome") == "":
			form_data["nome"] = "%%"
		else:
			form_data["nome"] = "%" + request.POST.get("nome") + "%"

		return "SELECT * FROM {tabella} WHERE codice LIKE '{codice}' AND provincia LIKE '{provincia}' AND nome LIKE '{nome}'".format(**form_data).replace(";", "") + ";"

	# Caso autostrada
	elif form_data["tabella"] == "autostrada":
		if request.POST.get("cod_naz") == "":
			form_data["cod_naz"] = "%%"
		else:
			form_data["cod_naz"] = "%" + request.POST.get("cod_naz") + "%"

		if request.POST.get("cod_eu") == "":
			form_data["cod_eu"] = "%%"
		else:
			form_data["cod_eu"] = "%" + request.POST.get("cod_eu") + "%"

		if request.POST.get("nome") == "":
			form_data["nome"] = "%%"
		else:
			form_data["nome"] = "%" +request.POST.get("nome") + "%"

		if request.POST.get("lunghezza") == "":
			form_data["lunghezza"] = "%%"
		else:
			form_data["lunghezza"] = request.POST.get("lunghezza")

		return "SELECT * FROM {tabella} WHERE cod_naz LIKE '{cod_naz}' AND cod_eu LIKE '{cod_eu}' AND nome LIKE '{nome}' AND lunghezza LIKE '{lunghezza}'".format(**form_data).replace(";", "") + ";"

	# Caso casello <- DA QUI
	else:
		sql_finale = "SELECT * FROM casello WHERE"

		if request.POST.get("codice") == "":
			sql_finale = sql_finale + " 1=1 AND"
		else:
			sql_finale = sql_finale + " codice LIKE '%" + request.POST.get("codice") + "%' AND"
		
		if request.POST.get("cod_naz") == " ":
			sql_finale = sql_finale + " 1=1 AND"
		else:
			sql_finale = sql_finale + " cod_naz LIKE '" + request.POST.get("cod_naz") + "' AND"

		if request.POST.get("comune") == " ":
			sql_finale = sql_finale + " 1=1 AND"
		else:
			sql_finale = sql_finale + " comune LIKE '" + request.POST.get("comune") + "' AND"

		if request.POST.get("nome") == "":
			sql_finale = sql_finale + " 1=1 AND"
		else:
			sql_finale = sql_finale + " nome LIKE '%" + request.POST.get("nome") + "%' AND"

		if request.POST.get("x") == "":
			sql_finale = sql_finale + " 1=1 AND"
		else:
			sql_finale = sql_finale + " x LIKE '" + request.POST.get("x") + "' AND"

		if request.POST.get("y") == "":
			sql_finale = sql_finale + " 1=1 AND"
		else:
			sql_finale = sql_finale + " y LIKE '" + request.POST.get("y") + "' AND"

		if request.POST.get("is_automatico") == "":
			sql_finale = sql_finale + " 1=1 AND"
		else:
			print(request.POST.get("is_automatico").lower())
			if request.POST.get("is_automatico").lower() == "true" or request.POST.get("is_automatico").lower() == "1":
				sql_finale = sql_finale + " is_automatico = 1 AND"
			elif request.POST.get("is_automatico").lower() == "false" or request.POST.get("is_automatico").lower() == "0":
				sql_finale = sql_finale + " is_automatico = 0 AND"
			else:
				sql_finale = sql_finale + " 1=1 AND"

		if request.POST.get("data_automazione") == "" or request.POST.get("data_automazione") is None:
			sql_finale = sql_finale + " 1=1"
		else:
			sql_finale = sql_finale + " data_automazione LIKE '" + request.POST.get("data_automazione") + "'"


		return sql_finale

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
		if (elemento[1], elemento[1]) not in listaUnica:
			listaUnica.append((elemento[1], elemento[1]))
	return listaUnica