import sqlite3
import json

with open('config.json', 'r') as myfile:

   data=myfile.read()
obj = json.loads(data)

print (obj["dbname"])

con = sqlite3.connect(obj["dbname"])
cur = con.cursor()

#res = cur.execute("SELECT nombre FROM Equipos")


cur.execute("SELECT * FROM EQUIPOS")


resultados = cur.fetchall()


for resultado in resultados:
    print(resultado)


con.close()