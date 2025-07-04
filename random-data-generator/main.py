# main.py

import functions_framework

# Questo "decoratore" registra la funzione 'hello_http' come una funzione HTTP.
# Google Cloud la invocherà quando l'URL della funzione viene chiamato.
@functions_framework.http
def hello_http(request):
    """
    Una semplice funzione HTTP che risponde a una richiesta web.
    Args:
        request (flask.Request): L'oggetto della richiesta HTTP.
    Returns:
        La risposta testuale da inviare al client.
    """
    # Puoi accedere ai dati della richiesta, come i parametri query.
    # Esempio: request.args.get('name')

    # Per ora, restituiamo un semplice saluto.
    return "Test Data"
