import subprocess
from flask_cors import CORS

comando_instalacion = ["pip", "install", "flask"]
subprocess.run(comando_instalacion)

from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)

from modelo import predecir_cluster

@app.route('/agrupar', methods=['POST'])
def predecir():
    datos_nuevo_registro = request.get_json()  # Suponiendo que los datos se envían como JSON desde la solicitud POST
    cluster_predicho = predecir_cluster(datos_nuevo_registro)
    return jsonify({'cluster_predicho': cluster_predicho})

if __name__ == '__main__':
    app.run(debug=True)

