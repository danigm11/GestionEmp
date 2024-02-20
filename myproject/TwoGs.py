from flask import Flask
import json
import Estadisticas

app = Flask(__name__)

with open('config.json', 'r') as myfile:

    data=myfile.read()
obj = json.loads(data)

print (obj["dbname"])

@app.route('/')
def hello():
    return "<p>Inicio</p>"

@app.route('/estadisticas')
def leerEstadistica():
    return Estadisticas.listaEstadisticas()

@app.route('/estadisticas/<string:KDA>')
def leer(KDA):
    return Estadisticas.listaEstadisticasKDA(KDA)

@app.route('/estadisticas/nuevas')
def nuevasEstadistica():
    return Estadisticas.nuevasEstadisticas()

@app.route('/estadisticas/borrar/<int:id>')
def borrarEstadistica(id):
    return Estadisticas.borrarEstadisticas(id)

@app.route('/estadisticas/editar/<int:id>')
def editarEstadistica(id):
    return Estadisticas.editarEstadisticas(id)

@app.route('/estadisticas/mostrar/<int:id>')
def verEstadistica(id):
    return Estadisticas.verEstadisticas(id)