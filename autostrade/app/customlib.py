from typing import Any
from unittest import result
import psycopg2

dbname = "pweb2"
username = "user"

def createConnection():
	conn = psycopg2.connect("dbname=" + dbname + " user=" + username)
	return conn

def getDataList(table: str) -> list[tuple]:
	conn = createConnection()
	cur = conn.cursor()

	print(table)
	
	cur.execute("SELECT * FROM {0};".format(table))
	result = cur.fetchall()
	conn.commit()

	cur.close()
	conn.close()
	return result

def addDataTable(table: str, data: dict):
	conn = createConnection()
	cur = conn.cursor()
	
	print(table)
	print(data)

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
	
	print(table)
	print(data)

	if table == "autostrada":
		cur.execute("UPDATE autostrada SET cod_eu='{cod_eu}', nome='{nome}', lunghezza={lunghezza} WHERE cod_naz='{cod_naz}';".format(**data))
	elif table == "comune": 
		cur.execute("UPDATE comune SET provincia='{provincia}', nome='{nome}' WHERE codice='{codice}';".format(**data))
	else:
		# RICODA DI CONTROLLARE LA COSA DELLA DATA
		cur.execute("UPDATE casello SET cod_naz='{cod_naz}', comune='{comune}', nome='{nome}', x='{x}', y='{y}', is_automatico={is_automatico}, data_automazione={data_automazione} WHERE codice={codice};".format(**data))

	conn.commit()
	cur.close()
	conn.close()
	return
