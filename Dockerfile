# Usa un'immagine Python ufficiale e leggera come base.
FROM python:3.11-slim

# Imposta la cartella di lavoro all'interno del container.
WORKDIR /app

# Copia prima il file delle dipendenze.
# Questo passaggio viene messo in cache da Docker, così non re-installerà
# le dipendenze ogni volta se non sono cambiate.
COPY requirements.txt requirements.txt

# Installa le dipendenze.
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del codice sorgente nella cartella di lavoro.
COPY . .

# Specifica il comando che avvierà il tuo server web quando il container parte.
# Usa Gunicorn, un server di produzione robusto per Python.
# Ascolterà sulla porta fornita dalla variabile d'ambiente PORT (che Cloud Run imposta a 8080).
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]