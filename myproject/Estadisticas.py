import sqlite3
import json
from flask import request

with open('config.json', 'r') as myfile:
  data=myfile.read()
obj = json.loads(data)

def listaEstadisticas():
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    cur.execute("SELECT * FROM Estadisticas")
    resultados = cur.fetchall()
    nombres = [i[0] for i in cur.description]

    lista_estadisticas = [
        {nombres[i]: row[i] for i in range(len(nombres))}
        for row in resultados
        ]
    
    con.close()
    return json.dumps(lista_estadisticas)

def listaEstadisticasKDApositivo(KDA):
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    cur.execute("SELECT * FROM Estadisticas WHERE KDA = ?",
            (KDA,)) 
    resultados = cur.fetchall()
    nombres = [i[0] for i in cur.description]

    lista_estadisticas = [
        {nombres[i]: row[i] for i in range(len(nombres))}
        for row in resultados
        ]
    
    con.close()
    return json.dumps(lista_estadisticas)

def nuevasEstadisticas():
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    new_estadistica= request.get_json()

    cur.execute("INSERT INTO Estadisticas (KDA, Asesinatos, Muertes, Asistencias, \"Partidos-jugados\", \"ID-Jugador\") VALUES (?, ?, ?, ?, ?, ?)",
            (new_estadistica['KDA'] ,new_estadistica['Asesinatos'] ,new_estadistica['Muertes'] ,new_estadistica['Asistencias'],new_estadistica['Partidos-jugados'] ,new_estadistica['ID-Jugador'] ))
    con.commit()
    con.close()
    return 'Estadísticas añadidas',200

def borrarEstadisticas(id):
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    cur.execute("DELETE FROM Estadisticas WHERE ID = ?",(id,))
    con.commit()
    con.close()
    return 'Estadísticas eliminadas', 200

def editarEstadisticas(id):
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    estadisticasEditadas = request.get_json()
    
    cur.execute("UPDATE ESTADISTICAS SET KDA = ?, Asesinatos = ?, Muertes = ?, Asistencias = ?, \"Partidos-jugados\" = ? WHERE \"ID-Jugador\" = ?",
                (estadisticasEditadas['KDA'], estadisticasEditadas['Asesinatos'], estadisticasEditadas['Muertes'], estadisticasEditadas['Asistencias'], estadisticasEditadas['Partidos-jugados'], id))
    con.commit()
    con.close()
    return 'Estadísticas actualizadas', 200


def verEstadisticas(id):
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    cur.execute("SELECT * FROM Estadisticas WHERE ID = ?",
            (id,))
    resultado = cur.fetchall()
    nombres = [i[0] for i in cur.description]

    lista_estadisticas = [
        {nombres[i]: row[i] for i in range(len(nombres))}
        for row in resultado
        ]
    
    con.close()
    return json.dumps(lista_estadisticas)