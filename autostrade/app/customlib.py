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
	print("no search")
	conn = createConnection()
	cur = conn.cursor()
	
	cur.execute("SELECT * FROM {0};".format(table))
	result = cur.fetchall()
	conn.commit()

	cur.close()
	conn.close()
	return result

def getDataListSearch(table: str, request) -> list[tuple]:
	print("yes search")
	print(request.method)
	print(HttpRequest)
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

def addDataTable(table: str, data: dict):
	conn = createConnection()
	cur = conn.cursor()

	if table == "autostrada":
		cur.execute("INSERT INTO autostrada (cod_naz, cod_eu, nome, lunghezza) VALUES ('{cod_naz}', '{cod_eu}', '{nome}', '{lunghezza}');".format(**data))
	elif table == "comune": 
		cur.execute("INSERT INTO comune (codice, provincia, nome) VALUES ('{codice}', '{provincia}', '{nome}');".format(**data))
	else:
		cur.execute("INSERT INTO casello (codice, cod_naz, comune, nome, x, y, is_automatico, data_automazione) VALUES ('{codice}', '{cod_naz}', '{comune}', '{nome}', '{x}', '{y}', '{is_automatico}', '{data_automazione}');".format(**data))

	conn.commit()
	cur.close()
	conn.close()
	return

def removeDataTable(table: str, data: dict):
	conn = createConnection()
	cur = conn.cursor()
	
	print(table)
	print(data)

	if table == "autostrada":
		cur.execute("DELETE FROM autostrada WHERE cod_naz = '{cod_naz}';".format(**data))
	elif table == "comune": 
		cur.execute("DELETE FROM comune WHERE codice = '{codice}';".format(**data))
	else:
		cur.execute("DELETE FROM casello WHERE codice = '{codice}' AND cod_naz = '{cod_naz}' AND comune = '{comune}';".format(**data))

	conn.commit()
	cur.close()
	conn.close()
	return

def updateDataTable(table: str, data: dict):
	conn = createConnection()
	cur = conn.cursor()

	if table == "autostrada":
		cur.execute("UPDATE autostrada SET cod_eu='{cod_eu}', nome='{nome}', lunghezza={lunghezza} WHERE cod_naz='{cod_naz}';".format(**data))
	elif table == "comune":
		cur.execute("UPDATE comune SET provincia='{provincia}', nome='{nome}' WHERE codice='{codice}';".format(**data))
	else:
		# RICODA DI CONTROLLARE LA COSA DELLA DATA
		if data.get("data_automazione") is None:
			cur.execute("UPDATE casello SET cod_naz='{cod_naz}', comune='{comune}', nome='{nome}', x='{x}', y='{y}', is_automatico={is_automatico}, data_automazione=NULL WHERE codice='{codice}' AND cod_naz='{cod_naz}' AND comune='{comune};".format(**data))
		else:
			cur.execute("UPDATE casello SET cod_naz='{cod_naz}', comune='{comune}', nome='{nome}', x='{x}', y='{y}', is_automatico={is_automatico}, data_automazione={data_automazione} WHERE codice='{codice}' AND cod_naz='{cod_naz}' AND comune='{comune};".format(**data))

	conn.commit()
	cur.close()
	conn.close()
	return

def sqlGen(form_data: dict, request) -> str:
	# Caso comune
	if form_data.get("tabella") == "comune":
		if request.POST.get("codice") is None:
			form_data["codice"] = "%%"
		else:
			form_data["codice"] = request.POST.get("codice")

		if request.POST.get("provincia") == " ":
			form_data["provincia"] = "%%"
		else:
			form_data["provincia"] = request.POST.get("provincia")

		if request.POST.get("nome") is None:
			form_data["nome"] = "%%"
		else:
			form_data["nome"] = "%" + request.POST.get("nome") + "%"

		form_data["provincia"] = "%%"

		return "SELECT * FROM {tabella} WHERE codice LIKE '{codice}' AND provincia LIKE '{provincia}' AND nome LIKE '{nome}'".format(**form_data).replace(";", "") + ";"

	# Caso autostrada
	elif form_data["tabella"] == "autostrada":
		if request.POST.get("cod_naz") is None:
			form_data["cod_naz"] = "%%"
		else:
			form_data["cod_naz"] = request.POST.get("cod_naz")

		if request.POST.get("cod_eu") is None:
			form_data["cod_eu"] = "%%"
		else:
			form_data["cod_eu"] = request.POST.get("cod_eu")

		if request.POST.get("nome") is None:
			form_data["nome"] = "%%"
		else:
			form_data["nome"] = request.POST.get("nome")

		if request.POST.get("lunghezza") is None:
			form_data["lunghezza"] = "%%"
		else:
			form_data["lunghezza"] = request.POST.get("lunghezza")

		print(form_data.get("tabella"))

		return "SELECT * FROM {tabella} WHERE cod_naz LIKE '{cod_naz}' AND cod_eu LIKE '{cod_eu}' AND nome LIKE '%{nome}%' AND lunghezza LIKE '{lunghezza}'".format(**form_data).replace(";", "") + ";"

	# Caso casello
	else:
		if request.POST.get("codice") is None:
			form_data["codice"] = "%%"
		else:
			form_data["codice"] = request.POST.get("codice")
		
		if request.POST.get("cod_naz") == " ":
			form_data["cod_naz"] = "%%"
		else:
			form_data["cod_naz"] = request.POST.get("cod_naz")

		if request.POST.get("comune") == " ":
			form_data["comune"] = "%%"
		else:
			form_data["comune"] = request.POST.get("comune")

		if request.POST.get("nome") is None:
			form_data["nome"] = "%%"
		else:
			form_data["nome"] = request.POST.get("nome")

		if request.POST.get("x") is None:
			form_data["x"] = "%%"
		else:
			form_data["x"] = request.POST.get("x")

		if request.POST.get("y") is None:
			form_data["y"] = "%%"
		else:
			form_data["y"] = request.POST.get("y")

		if request.POST.get("is_automatico") is None:
			form_data["is_automatico"] = "%%"
		else:
			form_data["is_automatico"] = request.POST.get("is_automatico")

		if request.POST.get("data_automazione") is None:
			form_data["data_automazione"] = "%%"
		else:
			form_data["data_automazione"] = request.POST.get("data_automazione")

		return "SELECT * FROM {tabella} WHERE codice LIKE '{codice}' AND cod_naz LIKE '{cod_naz}' AND comune LIKE '{comune}' AND nome LIKE '%{nome}%' AND x LIKE '{x}' AND y LIKE '{y}' AND is_automatico LIKE '{is_automatico}' AND data_automazione LIKE '{data_automazione}'".format(**form_data).replace(";", "") + ";"