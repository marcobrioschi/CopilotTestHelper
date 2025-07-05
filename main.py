import os
from flask import Flask, request, jsonify
from faker import Faker

# 1. Inizializza Faker una sola volta con la lingua italiana
faker = Faker("it_IT")

app = Flask(__name__)

# --- Metodo di supporto per la generazione dei dati (MODIFICATO) ---
def generate_test_data(datatype: str) -> str:
    """
    Invoca dinamicamente un metodo sull'istanza di Faker.
    Restituisce un errore se il metodo non è valido.
    """
    # 2. Controlla se l'istanza di faker ha un metodo con il nome 'datatype'
    if hasattr(faker, datatype) and callable(getattr(faker, datatype)):
        # 3. Se esiste, otteniamo il metodo e lo invochiamo
        method_to_call = getattr(faker, datatype)
        return method_to_call()
    else:
        # 4. Se non esiste, solleviamo un'eccezione che verrà gestita dall'endpoint
        raise ValueError(f"Il datatype '{datatype}' non è valido o supportato.")

# --- Endpoint di benvenuto ---
@app.route("/")
def hello_world():
    """Endpoint di benvenuto."""
    return "Servizio Cloud Run attivo."

# --- Endpoint di Callback Autenticazione ---
@app.route("/api/authCallback")
def auth_callback():
    """Risponde sempre con successo a una callback di autenticazione."""
    return "Authentication successful, now you can close this window", 200

# --- Endpoint di Generazione Dati (MODIFICATO) ---
@app.route("/testdata/generate")
def generate_data_endpoint():
    """
    Genera dati di test in base al parametro 'datatype' fornito nell'URL.
    Esempio: /testdata/generate?datatype=name
    """
    data_type = request.args.get('datatype')

    if not data_type:
        return jsonify({"error": "Il parametro 'datatype' è obbligatorio."}), 400

    try:
        # Chiama la logica di generazione dati
        test_data = generate_test_data(data_type)
        # Restituisce il dato generato come JSON per maggiore flessibilità
        return jsonify({"datatype": data_type, "data": test_data}), 200
    except ValueError as e:
        # Cattura l'errore se il datatype non è valido
        return jsonify({"error": str(e)}), 400

# --- Blocco per esecuzione locale ---
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))