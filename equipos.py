import sqlite3
import json
from flask import request 

with open('config.json', 'r') as myfile:
    data=myfile.read()
obj = json.loads(data)


#  petición GET TODOS LOS EQUIPOS

def get_equipos():
    conexion = sqlite3.connect(obj["dbname"])
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM EQUIPOS")
    resultados = cursor.fetchall()
    nombres = [i[0] for i in cursor.description]

    listaTeams =  [
        {nombres[i]: row[i] for i in range(len(nombres))}
        for row in resultados
    ]

    conexion.close()
    return json.dumps(listaTeams)

# http://localhost:5000/equipos/2 ** ayuda busqueda por id **

def obtener_equipo(id):
    conexion = sqlite3.connect(obj["dbname"])
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM EQUIPOS WHERE ID = ?", (id,))
    equipo = cursor.fetchone()
    nombres = [i[0] for i in cursor.description]

    detalles_equipo = {nombres[i]: equipo[i] for i in range(len(nombres))} if equipo else {}

    conexion.close()
    return json.dumps(detalles_equipo)

# http://localhost:5000/equipos/filtrar_por_nombre?nombre=T1 ** ayuda para filtrar en postman ** POR NOMBRE

def listaEquiposPorNombre(nombre_equipo):
    conexion = sqlite3.connect(obj["dbname"])
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM EQUIPOS WHERE Nombre = ?", (nombre_equipo,)) 
    resultados = cursor.fetchall()
    nombres = [i[0] for i in cursor.description]

    lista_equipos = [
        {nombres[i]: row[i] for i in range(len(nombres))}
        for row in resultados
    ]

    conexion.close()
    return json.dumps(lista_equipos)

# http://localhost:5000/equipos/filtrar_por_titulos_mundiales?num_titulos=2 ** ayuda para filtrar en postman ** POR NÚMERO DE TÍTULOS

def listaEquiposConMasDeNTitulosMundiales(num_titulos):
    conexion = sqlite3.connect(obj["dbname"])
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM EQUIPOS WHERE Titulos_Mundiales > ?", (num_titulos,))
    resultados = cursor.fetchall()
    nombres = [i[0] for i in cursor.description]

    lista_equipos = [
        {nombres[i]: row[i] for i in range(len(nombres))}
        for row in resultados
    ]

    conexion.close()
    return json.dumps(lista_equipos)

# http://localhost:5000/equipos POST  ** AÑADIR EQUIPO ** {
#     "Nombre": "TI",
#     "Region": "Asia",
#     "Titulos_Mundiales": 1,
#     "Titulos_Regionales": 2,
#     "Categoria": "Principal"
# }

def add_equipo():
    conexion = sqlite3.connect(obj["dbname"])
    cursor = conexion.cursor()
    new_equipo = request.get_json()
    cursor.execute("INSERT INTO EQUIPOS (Nombre, Region, Titulos_Mundiales, Titulos_Regionales, Categoria) VALUES (?, ?, ?, ?, ?)",
                   (new_equipo['Nombre'], new_equipo['Region'], new_equipo['Titulos_Mundiales'], new_equipo['Titulos_Regionales'], new_equipo['Categoria']))
    conexion.commit()
    conexion.close()
    return 'Equipo añadido',  200

# http://localhost:5000/equipos/3 PUT  ** MODIFICAR EQUIPO ** { importente añadir id a la url
#     "Nombre": "TI",
#     "Region": "Asia",
#     "Titulos_Mundiales": 1,
#     "Titulos_Regionales": 2,
#     "Categoria": "Principal"
# }

def update_equipo(id):
    conexion = sqlite3.connect(obj["dbname"])
    cursor = conexion.cursor()
    updated_equipo = request.get_json()
    cursor.execute("UPDATE EQUIPOS SET Nombre = ?, Region = ?, Titulos_Mundiales = ?, Titulos_Regionales = ?, Categoria = ? WHERE ID = ?",
                   (updated_equipo['Nombre'], updated_equipo['Region'], updated_equipo['Titulos_Mundiales'], updated_equipo['Titulos_Regionales'], updated_equipo['Categoria'], id))
    conexion.commit()
    conexion.close()
    return 'Equipo actualizado', 200

# http://localhost:5000/equipos/3 DELETE  BORRAR EQUIPOS

def delete_equipo(id):
    conexion = sqlite3.connect(obj["dbname"])
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM EQUIPOS WHERE ID = ?", (id,))
    conexion.commit()
    conexion.close()
    return 'Equipo eliminado', 200

# http://localhost:5000/equipos/1/jugadores   ** BUSCAR JUGADORES DE UN EQUIPO ** 

def get_jugadores(id_equipo):
    conexion = sqlite3.connect(obj["dbname"])
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Jugadores WHERE IDEquipo = ?", (id_equipo,))
    resultados = cursor.fetchall()
    nombres = [i[0] for i in cursor.description]

    listaJugadores = [
        {nombres[i]: row[i] for i in range(len(nombres))}
        for row in resultados
    ]

    conexion.close()
    return json.dumps(listaJugadores)


#   * AÑADIR JUGADORES *   http://localhost:5000/jugadoresD 
# {
#     "Nombre": "dani martin",
#     "Nacionalidad": "España",
#     "Edad": 100,
#     "Rol": "Variety",
#     "IDEquipo": 13
# }

def add_jugador():
    conexion = sqlite3.connect(obj["dbname"])
    cursor = conexion.cursor()
    new_jugador = request.get_json()
    cursor.execute("INSERT INTO Jugadores (Nombre, Nacionalidad, Edad, Rol, IDEquipo) VALUES (?, ?, ?, ?, ?)",
                   (new_jugador['Nombre'], new_jugador['Nacionalidad'], new_jugador['Edad'], new_jugador['Rol'], new_jugador['IDEquipo']))
    conexion.commit()
    conexion.close()
    return 'Jugador añadido', 201
