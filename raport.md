# Laboratorul nr. 5 – Aplicația web: recon, conținut și exploatare

**Student:** Artur Postolachi  
**Universitatea:** Universitatea Tehnică a Moldovei  
**Specialitatea:** Securitate informațională

## 1. Scopul lucrării

Scopul lucrării este dezvoltarea unor instrumente Python pentru analiza aplicațiilor web, identificarea informațiilor oferite de server și verificarea funcționării instrumentelor prin teste automate.

## 2. Lucrarea A – Recon web

**A1 – Fingerprinting**

Am realizat o cerere HTTP utilizând biblioteca `requests` și am extras antetele serverului.

Rezultate pe serverul local:
- Cod HTTP: 200
- Server: SimpleHTTP Python/3.15.0
- X-Powered-By: None

**A2 – Analiza robots.txt**

Am verificat existența fișierului `robots.txt`.

Rezultat: HTTP 404. Fișierul nu a fost găsit pe serverul local, iar programul a gestionat corect răspunsul.

**A3 – Descoperirea directoarelor**

Am utilizat o listă de directoare și am verificat codurile HTTP returnate.

Directoare găsite:
- admin
- login
- uploads

Directoare negăsite: backup, config, test, phpmyadmin.

**A4 – Extragerea linkurilor**

Am utilizat biblioteca `re` și expresii regulate pentru extragerea linkurilor din HTML.

Rezultat: 3 linkuri unice – `admin/`, `login/`, `uploads/`.

**A5 – Clientul HTTP**

Am creat fișierul `client.py` cu funcțiile `cere()` și `exista()`. Timpul de așteptare este configurat prin `TIMEOUT = 10` în `comun.py`.

**A6 – Argumente din terminal**

Am integrat biblioteca `argparse`, care permite transmiterea adresei serverului și a unui fișier opțional `--wordlist`.

**A7 – Fișier JSON și teste**

Am creat automat fișierul `arsenal/web/fisa.json`, care conține adresa țintei, informații despre server, directoarele identificate și linkurile extrase.

Am verificat funcționarea clientului utilizând `pytest`.

Rezultat: **2 passed**.

## 3. Mediul de testare

Testele au fost efectuate pe un server HTTP local, pornit folosind Python la adresa `http://127.0.0.1:8000`.

Directoarele verificate au fost create special pentru testare.

Rezultatele nu reprezintă analiza aplicației DVWA/Metasploitable2.

## 4. Lucrarea B – Stadiu

Testele privind SQL Injection și Local File Inclusion nu au fost efectuate, deoarece ținta autorizată DVWA nu a fost încă pregătită.

Pentru prevenirea acestor vulnerabilități sunt importante interogările SQL parametrizate, validarea căilor și verificarea accesului pe server.

## 5. Concluzii

În cadrul Lucrării A am realizat un program Python care analizează răspunsurile HTTP, verifică fișierul robots.txt, identifică directoare, extrage linkuri și salvează rezultatele în format JSON.

Am utilizat bibliotecile `requests`, `re`, `argparse` și `json`. Testele automate au confirmat funcționarea clientului HTTP pe mediul local de testare.

Lucrarea mi-a permis să înțeleg principiile recunoașterii web și importanța testării aplicațiilor într-un mediu autorizat.
### B6 – Apărarea împotriva SQL Injection

Am creat fișierul arsenal/web/aparare_sqli.py,
utilizând biblioteca sqlite3.

Am construit o bază de date temporară și am
folosit interogări SQL parametrizate.

Rezultatele obținute:
- Utilizator existent: [('artur', 'x')]
- Utilizator inexistent: []
- Test protecție SQL Injection: []

Concluzie:
Interogarea parametrizată tratează valorile
introduse de utilizator ca date, nu ca instrucțiuni
SQL, prevenind acest tip de SQL Injection.