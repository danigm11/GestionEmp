from flask import Flask, request, jsonify, g
import sqlite3

app = Flask(__name__)
DATABASE = "TwoGs.db"

# Establecer la conexión a la base de datos
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
    

# Insertar valores de ejemplo
insert_Estadisticas_query = """
INSERT INTO Estadísticas (KDA, Asesinatos, Muertes, Asistencias, "Partidos jugados", "ID-Jugador") VALUES
(10, 2, 8, 15, 1, 1),
(8, 5, 6, 14, 2, 2),
(12, 3, 9, 18, 3, 3),
(6, 4, 7, 12, 4, 4),
(15, 1, 10, 20, 5, 5),
(9, 6, 8, 16, 6, 6),
(11, 2, 9, 14, 7, 7),
(14, 3, 11, 22, 8, 8),
(7, 5, 6, 13, 9, 9),
(13, 2, 12, 19, 10, 10);
"""
with app.app_context():
    cur = get_db().cursor()
    cur.executescript(insert_Estadisticas_query)
    cur.close()


# Endpoint para obtener estadísticas con KDA positivo
@app.route('/estadisticas/positivas', methods=['GET'])
def get_estadisticas_positivas():
    cur = get_db().cursor()
    cur.execute('SELECT * FROM Estadísticas WHERE KDA > 0')
    data = cur.fetchall()
    return jsonify(data)

# Endpoint para obtener información de un solo registro
@app.route('/estadisticas/<int:estadistica_id>', methods=['GET'])
def get_estadistica(estadistica_id):
    cur = get_db().cursor()
    cur.execute('SELECT * FROM Estadísticas WHERE ID = ?', (estadistica_id,))
    data = cur.fetchone()
    if data:
        return jsonify(data)
    else:
        return jsonify({'message': 'Estadística no encontrada'}), 404

# Endpoint para crear un nuevo registro
@app.route('/estadisticas', methods=['POST'])
def create_estadistica():
    new_data = request.json
    cur = get_db().cursor()
    cur.execute('INSERT INTO Estadísticas (KDA, Asesinatos, Muertes, Asistencias, "Partidos jugados", "ID-Jugador") VALUES (?, ?, ?, ?, ?, ?)',
                (new_data['KDA'], new_data['Asesinatos'], new_data['Muertes'], new_data['Asistencias'], new_data['Partidos jugados'], new_data['ID-Jugador']))
    get_db().commit()
    return jsonify({'message': 'Estadística creada correctamente'}), 201

# Endpoint para modificar un registro existente
@app.route('/estadisticas/<int:estadistica_id>', methods=['PUT'])
def update_estadistica(estadistica_id):
    updated_data = request.json
    cur = get_db().cursor()
    cur.execute('UPDATE Estadísticas SET KDA=?, Asesinatos=?, Muertes=?, Asistencias=?, "Partidos jugados"=?, "ID-Jugador"=? WHERE ID=?',
                (updated_data['KDA'], updated_data['Asesinatos'], updated_data['Muertes'], updated_data['Asistencias'], updated_data['Partidos jugados'], updated_data['ID-Jugador'], estadistica_id))
    get_db().commit()
    return jsonify({'message': 'Estadística actualizada correctamente'})

# Endpoint para eliminar un registro
@app.route('/estadisticas/<int:estadistica_id>', methods=['DELETE'])
def delete_estadistica(estadistica_id):
    cur = get_db().cursor()
    cur.execute('DELETE FROM Estadísticas WHERE ID = ?', (estadistica_id,))
    get_db().commit()
    return jsonify({'message': 'Estadística eliminada correctamente'})

if __name__ == '__main__':
    app.run(debug=True)