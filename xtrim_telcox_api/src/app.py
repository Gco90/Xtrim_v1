
from flask import Flask, jsonify
from flask_cors import CORS
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)  # permite llamadas desde http://localhost:4200


#funcion que genera los datos aleatorios de consumo para simular las respuesta de BSS
def make_mock_consumo(cliente_nombre="Cliente Demo"):
    return {
        "cliente": {"id": 1, "nombre": cliente_nombre},
        "plan_actual": "Mega Fibra Plus",    
        "datos_gb": round(random.uniform(0.0, 20.0), 2),   #Consumo de datos (valor aleatorio)
        "datos_limite_gb": 20,                             #Limite de gb contratados
        "minutos": random.randint(0, 500),                 #Consumo de minutos(Valor aleatorio)
        "minutos_limite": 500,                             #Limite de minutos
        "sms": random.randint(0, 500),                     #Consumo de SMS(Valor Aletarorio)
        "sms_limite": 500,                                 #Limite de SMS
        "ultima_actualizacion": datetime.utcnow().isoformat() + "Z",
        "saldo_cuenta": round(random.uniform(0.0, 40.0), 2), # Saldo aleatorio de cuenta
        "proximo_corte": "2025-11-25",
        "ultima_factura": round(random.uniform(0.0, 50.0), 2) #Valor de la ultima Factura
    }

#EndPoit principal que devuelve en datos json los consumos del cliente por defecto
@app.route("/api/consumo", methods=["GET"])
def consumo():
    data = make_mock_consumo("Gianni Condo")
    return jsonify(data), 200

@app.route("/api/consumo/<int:cliente_id>", methods=["GET"])
def consumo_cliente(cliente_id):
    data = make_mock_consumo(f"Cliente {cliente_id}")
    return jsonify(data), 200

@app.errorhandler(500)
def on_error(e):
    return jsonify({"error": "Internal Server Error"}), 500

#Degub en True para ambiente de desarrollo
#Corre en local host en el puerto 5000
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
