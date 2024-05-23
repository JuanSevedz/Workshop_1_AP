from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Función para cargar los datos del catálogo desde data.json
def load_catalog_data():
    with open('data.json', 'r') as f:
        catalog_data = json.load(f)
    return catalog_data

# Mostrar el catálogo de vehículos
@app.route('/catalog')
def show_catalog():
    catalog_data = load_catalog_data()
    return jsonify(catalog_data)

# Agregar un vehículo al catálogo
@app.route('/add_vehicle', methods=['POST'])
def add_vehicle():
    # Aquí deberías procesar los datos del formulario y agregar el vehículo al catálogo
    # Actualiza data.json con el nuevo vehículo
    # Retorna una respuesta JSON indicando si la operación fue exitosa o no
    return jsonify({"message": "Vehicle added successfully"})

# Agregar un motor al catálogo
@app.route('/add_engine', methods=['POST'])
def add_engine():
    # Aquí deberías procesar los datos del formulario y agregar el motor al catálogo
    # Actualiza data.json con el nuevo motor
    # Retorna una respuesta JSON indicando si la operación fue exitosa o no
    return jsonify({"message": "Engine added successfully"})

# Mostrar vehículos de un tipo específico
@app.route('/specific_type', methods=['GET'])
def show_specific_type():
    # Aquí deberías filtrar los datos del catálogo por el tipo de vehículo solicitado
    # Retorna una respuesta JSON con los vehículos del tipo especificado
    return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)
