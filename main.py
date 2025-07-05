# main.py
import os
from flask import Flask

# Crea un'istanza dell'applicazione Flask.
# Il nome 'app' è importante perché è quello che Gunicorn cercherà (vedi il Dockerfile).
app = Flask(__name__)

# Definisci una "rotta", cioè un URL a cui l'app risponderà.
# In questo caso, risponderà all'URL radice ('/').
@app.route("/")
def hello_world():
    """Risponde con un semplice messaggio di saluto."""
    # Puoi ancora usare le variabili d'ambiente se necessario.
    name = os.environ.get("NAME", "Mondo")
    return f"Ciao, {name}! Questo è un servizio Cloud Run."

if __name__ == "__main__":
    # Questa parte serve solo per testare in locale.
    # Cloud Run NON la eseguirà, userà il comando Gunicorn del Dockerfile.
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))