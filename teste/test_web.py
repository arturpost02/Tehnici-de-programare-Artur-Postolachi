from arsenal.web.client import exista

# Verificam daca pagina exista
def test_exista():
    assert exista("http://127.0.0.1:8000/admin/")

# Verificam daca pagina lipseste
def test_lipsa():
    assert not exista("http://127.0.0.1:8000/nu_exista_123456/")
