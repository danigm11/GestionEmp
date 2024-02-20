from flask import Flask, request
import Jugadores
import Equipos
import json
import Torneos

app = Flask(__name__)

with open('config.json', 'r') as myfile:
    data=myfile.read()
obj = json.loads(data)


@app.route('/')
def hello():
    return "<p><Inicio</p>"

# End points tabla equipos /////////////////// Daniel Martín Sáiz //////////////

# Muestra la lista de todos los equipos.
@app.route('/equipos', methods=['GET'])
def lista_equipos():
    return Equipos.get_equipos()

#  Muestra los datos del equipo con esa id.
@app.route('/equipos/<int:id>', methods=['GET'])
def obtener_equipo(id):
    return Equipos.obtener_equipo(id)

# Muestra los dados del equipo con ese nombre, variable hay que pasarla mediante Params
@app.route('/equipos/filtrar_por_nombre', methods=['GET'])
def filtrar_equipos_por_nombre():
    nombre_equipo = request.args.get('nombre')
    return Equipos.listaEquiposPorNombre(nombre_equipo)


# Muestra los dados del equipo con más mundiales que los pasados por id, variable hay que pasarla mediante Params
@app.route('/equipos/filtrar_por_titulos_mundiales', methods=['GET'])
def filtrar_equipos_por_titulos_mundiales():
    num_titulos = request.args.get('num_titulos')
    return Equipos.listaEquiposConMasDeNTitulosMundiales(num_titulos)

# Añadir equipo
@app.route('/equipos', methods=['POST'])
def añadir_equipo():
    return Equipos.add_equipo()

# Modificar equipo
@app.route('/equipos/<int:id>', methods=['PUT'])
def modificar_equipo(id):
    return Equipos.update_equipo(id)

# Borrar equipo
@app.route('/equipos/<int:id>', methods=['DELETE'])
def borrar_equipo(id):
    return Equipos.delete_equipo(id)

# Ver jugadores en un equipo, conexión entre tablas
@app.route('/equipos/<int:id_equipo>/jugadores', methods=['GET'])
def obtener_jugadores_equipo(id_equipo):
    return Equipos.get_jugadores(id_equipo)

# Añadir jugadores, necesario para la petición anterior
@app.route('/jugadoresD', methods=['POST'])
def nuevo_jugador():
    return Equipos.add_jugador()

# FÍN End points tabla equipos // Daniel Martín Sáiz ////////////////////////////////////////


# End points tabla torneos /////////////////// Daniel García Mesa //////////////
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

# FÍN End points tabla torneos // Daniel García Mesa ////////////////////////////////////////



# Principio End points tabla Jugadores // Adolfo Burgos Belgrano ////////////////////////////////////////
@app.route('/Jugadores')
def leerJugadores():
    return Jugadores.listaJugadores()

@app.route('/Jugadores/edad/<int:edad>')
def leer(edad):
    return Jugadores.listaJugadoresPorEdad(edad)

@app.route('/Jugadores/nuevo')
def nuevoJugador():
    return Jugadores.nuevoJugador()

@app.route('/Jugadores/borrar/<int:id>')
def borrarJugador(id):
    return Jugadores.borrarJugador(id)

@app.route('/Jugadores/modificar/<int:id>')
def modificarJugador(id):
    return Jugadores.ModificarJugador(id)

@app.route('/Jugadores/mostrar/<int:id>')
def verJugador(id):
    return Jugadores.verJugador(id)

# FÍN End points tabla Jugadores // Adolfo Burgos Belgrano ////////////////////////////////////////