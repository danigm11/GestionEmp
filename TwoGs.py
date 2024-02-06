from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<p>Hello, World!</p>"


@app.route('/torneos')
def torneo():
    return "<p>Torneos</p>"

@app.route('/equipos')
def equipos():
    return "<pEquipos</p>"