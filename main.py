import os
from flask import Flask, request, jsonify

# Crea un'istanza dell'applicazione Flask.
app = Flask(__name__)

# --- Metodo di supporto per la generazione dei dati ---
def generate_test_data(datatype: str) -> str:
    """
    Logica per generare i dati. Prende in ingresso il datatype
    e per ora restituisce una stringa fissa.
    """
    # In futuro, qui potrai inserire la logica basata sul valore di 'datatype'.
    print(f"Generazione dati richiesta per il tipo: {datatype}")
    return "test"

# --- Endpoint Esistente ---
@app.route("/")
def hello_world():
    """Endpoint di benvenuto."""
    return "Servizio Cloud Run attivo."

# --- NUOVO ENDPOINT 1: Callback di Autenticazione ---
@app.route("/api/authCallback")
def auth_callback():
    """Risponde sempre con successo a una callback di autenticazione."""
    response_text = "Authentication successful, now you can close this window"
    return response_text, 200

# --- NUOVO ENDPOINT 2: Generazione Dati di Test ---
@app.route("/testdata/generate")
def generate_data_endpoint():
    """
    Genera dati di test in base al parametro 'datatype' fornito nell'URL.
    Esempio: /testdata/generate?datatype=user
    """
    # Ottieni il valore del parametro 'datatype' dall'URL
    data_type = request.args.get('datatype')

    # Controlla se il parametro è stato fornito
    if not data_type:
        error_message = {"error": "Il parametro 'datatype' è obbligatorio."}
        return jsonify(error_message), 400

    # Invoca il metodo che genera i dati e restituisce il risultato
    test_data = generate_test_data(data_type)
    return test_data, 200

# --- Blocco per esecuzione locale (non usato da Cloud Run) ---
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))