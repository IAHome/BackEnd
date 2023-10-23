import subprocess
from flask_cors import CORS

comando_instalacion = ["pip", "install", "flask"]
subprocess.run(comando_instalacion)

from flask import Flask, request, jsonify
from modelo import Modelo

app = Flask(__name__)
CORS(app)
modelo_instancia = Modelo()

@app.route('/agrupar', methods=['POST'])

def agrupar():
    data = request.get_json()
    parametros = ['edad', 'genero', 'comuna', 'tipoVivienda', 'totalPersonasH', 'sumaIngresosAux','sumaIngresosLAV', 'sumaIngresosExt', 'sumaGastos']
    for param in parametros:
        if param not in data:
            return jsonify({'error': f'Falta el parámetro {param}'}), 400

    grupo = modelo_instancia.agrupar(**data)
    

    return jsonify({'grupo': grupo})

if __name__ == '__main__':
    app.run(debug=True)
