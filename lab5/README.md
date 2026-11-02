# Laboratorul 5

Instrumente pentru recon web, client HTTP și demonstrații locale. Rezultatele și limitele exercițiilor sunt descrise în [raport](raport.md).

- `arsenal/web/`: programele și fișa JSON.
- `arsenal/comun.py`: configurarea clientului HTTP.
- `teste/test_web.py`: testele clientului HTTP.
- `web_lab_Artur_Postolachi.zip`: arhiva originală păstrată ca referință; conținutul arhivei nu a fost modificat.

Din rădăcina depozitului, intră în folderul laboratorului:

```powershell
cd lab5
python -m pip install requests pytest
```

Pentru recon, pornește mai întâi serverul local folosit ca țintă, apoi:

```powershell
python -m arsenal.web.recon http://127.0.0.1:8000
```

Testele existente necesită un server pe `127.0.0.1:8000` care răspunde cu HTTP 200 la `/admin/` și HTTP 404 la `/nu_exista_123456/`:

```powershell
python -m pytest -q teste/test_web.py
```

Demonstrațiile locale independente de server:

```powershell
python -m arsenal.web.aparare_sqli
python -m arsenal.web.b2_sqlite
python -m arsenal.web.b4_fisiere
python -m arsenal.web.b5_union
```

`arsenal/web/b1_test.py` utilizează ținta configurată în fișier; rulează-l numai când mediul de laborator respectiv este disponibil.
