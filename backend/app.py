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
    print("Dati ricevuti da Angular:", data) # <--- AGGIUNGI QUESTO
    
    success = db.insert_delivery(data)
    if success:
        return jsonify({"message": "OK"}), 201
    else:
        # Se fallisce, mandiamo un errore più chiaro
        return jsonify({"error": "Errore interno al DB"}), 500
    
@app.route('/deliveries/<int:delivery_id>/status', methods=['PUT'])
def update_status(delivery_id):
    data = request.json
    new_status = data.get('status')
    
    if not new_status:
        return jsonify({"error": "Stato mancante"}), 400
        
    success = db.update_delivery_status(delivery_id, new_status)
    if success:
        return jsonify({"message": "Stato aggiornato"}), 200
    else:
        return jsonify({"error": "Errore aggiornamento"}), 500

if __name__ == '__main__':
    # Inizializza la tabella all'avvio se necessario
    db.init_database()
    app.run(debug=True, port=5000)