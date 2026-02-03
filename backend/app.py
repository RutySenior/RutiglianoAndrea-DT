from flask import Flask, jsonify, request
from flask_cors import CORS
from DatabaseWrapper import DatabaseWrapper

app = Flask(__name__)
CORS(app) # Abilita le chiamate dal frontend Angular

db = DatabaseWrapper()

@app.route('/deliveries', methods=['GET'])
def get_deliveries():
    deliveries = db.get_all_deliveries()
    return jsonify(deliveries)

@app.route('/deliveries', methods=['POST'])
def add_delivery():
    data = request.json
    
    # Validazione base
    required_fields = ['tracking_code', 'recipient', 'address', 'time_slot']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Dati mancanti"}), 400
    
    success = db.insert_delivery(data)
    if success:
        return jsonify({"message": "Consegna creata"}), 201
    else:
        return jsonify({"error": "Errore durante il salvataggio o tracking duplicato"}), 500

if __name__ == '__main__':
    # Inizializza la tabella all'avvio se necessario
    db.init_database()
    app.run(debug=True, port=5000)