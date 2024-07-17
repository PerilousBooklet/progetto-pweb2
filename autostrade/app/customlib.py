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
	cur.execute("SELECT * FROM {0}".format(table))
	result = cur.fetchall()
	conn.commit()
	print(result)
	cur.close()
	conn.close()
	return result

def addDataTable(table: str, data: dict):
	data["table"] = table

	conn = createConnection()
	cur = conn.cursor()
	
	print(table)
	print(data)

	if table == "autostrada":
		cur.execute("INSERT INTO {table} (cod_naz, cod_eu, nome, lunghezza) VALUES ('{cod_naz}', '{cod_eu}', '{nome}', '{lunghezza}')".format(**data))
	elif table == "comune": 
		cur.execute("INSERT INTO {table} (codice, provincia, nome) VALUES ('{codice}', '{provincia}', '{nome}')".format(**data))
	else:
		cur.execute("INSERT INTO {table} (codice, cod_naz, comune, nome, x, y, is_automatico, data_automazione) VALUES ('{codice}', '{cod_naz}', '{comune}', '{nome}', '{x}', '{y}', '{is_automatico}', '{data_automazione}')".format(**data))

	conn.commit()
	cur.close()
	conn.close()
	return