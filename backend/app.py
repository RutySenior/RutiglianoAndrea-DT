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

if __name__ == '__main__':
    # Inizializza la tabella all'avvio se necessario
    db.init_database()
    app.run(debug=True, port=5000)