from flask import Flask
import json
import Torneos

app = Flask(__name__)

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


