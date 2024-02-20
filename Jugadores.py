import sqlite3
import json
from flask import request

with open('config.json', 'r') as myfile:
  data=myfile.read()
obj = json.loads(data)

def listaJugadores():
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    cur.execute("SELECT * FROM JUGADORES")
    resultados = cur.fetchall()
    nombres = [i[0] for i in cur.description]

    lista_jugadores = [
        {nombres[i]: row[i] for i in range(len(nombres))}
        for row in resultados
        ]

    con.close()
    return json.dumps(lista_jugadores)

def listaJugadoresPorEdad(edad):
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    cur.execute("SELECT * FROM JUGADORES WHERE EDAD = ?",(edad,)),
    resultados = cur.fetchall()
    nombres = [i[0] for i in cur.description]

    lista_jugadores = [
        {nombres[i]: row[i] for i in range(len(nombres))}
        for row in resultados
        ]

    con.close()
    return json.dumps(lista_jugadores)

def nuevoJugador():
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    new_jugador= request.get_json()

    cur.execute("INSERT INTO JUGADORES (Nombre, Nacionalidad, Edad, Rol, IDEquipo) VALUES (?, ?, ?, ?, ?)",
            (new_jugador['nombre'],new_jugador['nacionalidad'] ,new_jugador['edad'] ,new_jugador['rol'] ,new_jugador['IDEquipo'] ))
    con.commit()
    con.close()
    return 'Jugador añadido',200

def borrarJugador(id):
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    cur.execute("DELETE FROM JUGADORES WHERE id = ?",(id,)),
    con.commit()
    con.close()
    return 'Jugador eliminado',200

def ModificarJugador(id):
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    modificar_jugador= request.get_json()

    cur.execute("UPDATE JUGADORES SET Nombre = ?, Nacionalidad = ?, Edad = ?, Rol = ?, IDEquipo = ? WHERE ID = ?",
            ( modificar_jugador['nombre'], modificar_jugador['nacionalidad'] ,modificar_jugador['edad'] ,modificar_jugador['rol'] ,modificar_jugador['IDEquipo'] , id))
    con.commit()
    con.close()
    return 'Jugador modificado',200

def verJugador(id):
    con = sqlite3.connect(obj["dbname"])
    cur = con.cursor()
    cur.execute("SELECT * FROM JUGADORES WHERE ID = ?",
            (id,))
    resultado = cur.fetchall()
    nombres = [i[0] for i in cur.description]

    lista_jugadores = [
      {nombres[i]: row[i] for i in range(len(nombres))}
      for row in resultado
      ]
    
    con.close()
    return json.dumps(lista_jugadores)