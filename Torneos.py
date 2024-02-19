import sqlite3
import json
from flask import request

with open('config.json', 'r') as myfile:
  data=myfile.read()
obj = json.loads(data)

def listaTorneos():
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    cur.execute("SELECT * FROM TORNEOS")
    resultados = cur.fetchall()
    nombres = [i[0] for i in cur.description]

    lista_torneos = [
        {nombres[i]: row[i] for i in range(len(nombres))}
        for row in resultados
        ]
    
    con.close()
    return json.dumps(lista_torneos)

def listaTorneosPorSede(sede):
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    cur.execute("SELECT * FROM TORNEOS WHERE Sede = ?",
            (sede,))
    resultados = cur.fetchall()
    nombres = [i[0] for i in cur.description]

    lista_torneos = [
        {nombres[i]: row[i] for i in range(len(nombres))}
        for row in resultados
        ]
    
    con.close()
    return json.dumps(lista_torneos)

def nuevoTorneo():
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    new_torneo= request.get_json()

    cur.execute("INSERT INTO TORNEOS (Nombre, Sede, Fecha, Premio, Categoria) VALUES (?, ?, ?, ?, ?)",
            (new_torneo['Nombre'],new_torneo['Sede'] ,new_torneo['Fecha'] ,new_torneo['Premio'] ,new_torneo['Categoria'] ))
    con.commit()
    con.close()
    return 'Torneo añadido',200

def borrarTorneo(id):
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    cur.execute("DELETE FROM TORNEOS WHERE ID = ?",(id,))
    con.commit()
    con.close()
    return 'Torneo eliminado', 200

def editarTorneo(id):
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    torneoEditado = request.get_json()
    cur.execute("UPDATE TORNEOS SET Nombre = ?, Sede = ?, Fecha = ?, Premio = ?, Categoria = ? WHERE ID = ?",
            (torneoEditado['Nombre'], torneoEditado['Sede'], torneoEditado['Fecha'], torneoEditado['Premio'], torneoEditado['Categoria'], id))
    con.commit()
    con.close()
    return 'Equipo actualizado', 200

def verTorneo(id):
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    cur.execute("SELECT * FROM TORNEOS WHERE ID = ?",
            (id,))
    resultado = cur.fetchall()
    nombres = [i[0] for i in cur.description]

    lista_torneos = [
      {nombres[i]: row[i] for i in range(len(nombres))}
      for row in resultado
      ]
    
    con.close()
    return json.dumps(lista_torneos)