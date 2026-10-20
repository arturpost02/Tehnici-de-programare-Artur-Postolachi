import requests
from arsenal.comun import TIMEOUT

# Trimite o cerere HTTP
def cere(url, **kw):
    kw.setdefault("timeout", TIMEOUT)
    return requests.get(url, **kw)

# Verifica daca o pagina raspunde cu 200
def exista(url):
    return cere(url).status_code == 200
