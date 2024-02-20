from flask import Flask, request
import sqlite3
import json 
import equipos
import json
import Torneos

app = Flask(__name__)

# End points tabla equipos // Daniel Martín Sáiz

with open('config.json', 'r') as myfile:
    data=myfile.read()
obj = json.loads(data)

# Muestra la lista de todos los equipos.
@app.route('/equipos', methods=['GET'])
def lista_equipos():
    return equipos.get_equipos()

#  Muestra los datos del equipo con esa id.
@app.route('/equipos/<int:id>', methods=['GET'])
def obtener_equipo(id):
    return equipos.obtener_equipo(id)

# Muestra los dados del equipo con ese nombre, variable hay que pasarla mediante Params
@app.route('/equipos/filtrar_por_nombre', methods=['GET'])
def filtrar_equipos_por_nombre():
    nombre_equipo = request.args.get('nombre')
    return equipos.listaEquiposPorNombre(nombre_equipo)


# Muestra los dados del equipo con más mundiales que los pasados por id, variable hay que pasarla mediante Params
@app.route('/equipos/filtrar_por_titulos_mundiales', methods=['GET'])
def filtrar_equipos_por_titulos_mundiales():
    num_titulos = request.args.get('num_titulos')
    return equipos.listaEquiposConMasDeNTitulosMundiales(num_titulos)

# Añadir equipo
@app.route('/equipos', methods=['POST'])
def añadir_equipo():
    return equipos.add_equipo()

# Modificar equipo
@app.route('/equipos/<int:id>', methods=['PUT'])
def modificar_equipo(id):
    return equipos.update_equipo(id)

# Borrar equipo
@app.route('/equipos/<int:id>', methods=['DELETE'])
def borrar_equipo(id):
    return equipos.delete_equipo(id)

# Ver jugadores en un equipo, conexión entre tablas
@app.route('/equipos/<int:id_equipo>/jugadores', methods=['GET'])
def obtener_jugadores_equipo(id_equipo):
    return equipos.get_jugadores(id_equipo)

# Añadir jugadores, necesario para la petición anterior
@app.route('/jugadoresD', methods=['POST'])
def nuevo_jugador():
    return equipos.add_jugador()

# FÍN End points tabla equipos // Daniel Martín Sáiz


with open('config.json', 'r') as myfile:

   data=myfile.read()
obj = json.loads(data)

print (obj["dbname"])

@app.route('/')
def hello():
    return "<p><Inicio</p>"

@app.route('/torneos')
def leerTorneos():
    return Torneos.listaTorneos()

@app.route('/torneos/<string:sede>')
def leer(sede):
    return Torneos.listaTorneosPorSede(sede)

@app.route('/torneos/nuevo')
def nuevoTorneo():
    return Torneos.nuevoTorneo()

@app.route('/torneos/borrar/<int:id>')
def borrarTorneos(id):
    return Torneos.borrarTorneo(id)

@app.route('/torneos/editar/<int:id>')
def editarTorneos(id):
    return Torneos.editarTorneo(id)

@app.route('/torneos/mostrar/<int:id>')
def verTorneo(id):
    return Torneos.verTorneo(id)

@app.route('/equipos')
def equipos():
    return "<pEquipos</p>"


