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
### B1 – Cerere HTTP normală

Am utilizat clientul HTTP creat anterior pentru
a trimite o cerere GET către serverul Kali Linux.

Adresa: http://192.168.56.101:8080

Rezultate:
- Cod HTTP: 200
- Lungime răspuns: 9 octeți
- Conținut: Lab 5 OK

### Test pregătitor pentru B2 – Compararea răspunsurilor

Am trimis două cereri HTTP cu parametri diferiți:
- id=1
- id=2

Rezultate:
- Răspuns ID 1: 9 octeți
- Răspuns ID 2: 9 octeți
- Răspunsurile sunt identice.

Concluzie:
Serverul HTTP simplu returnează același conținut
indiferent de valoarea parametrului id.

Testul demonstrează compararea răspunsurilor HTTP,
dar nu confirmă o vulnerabilitate SQL Injection.
## Rezultatele demonstrațiilor locale B2–B5

### B2 – SQL Injection

Am creat o bază de date SQLite temporară, cu trei utilizatori fictivi, și am comparat o interogare nesigură cu una parametrizată.

Rezultate:
- Cerere normală: 1 utilizator.
- Intrare SQL de test: 3 utilizatori.
- Interogare parametrizată: 0 utilizatori.

### B3 – Testarea automată a intrărilor

Am verificat patru tipuri de intrări: ID existent, ID inexistent, text cu apostrof și intrarea SQL din B2.

Am observat că interogarea nesigură poate produce erori sau rezultate nedorite, în timp ce interogarea parametrizată tratează valorile ca date.

### B4 – Protecția împotriva LFI

Am utilizat biblioteca `pathlib` pentru verificarea căilor către fișiere.

Rezultate:
- Fișier permis: citit cu succes.
- Fișier inexistent: mesaj corespunzător.
- Cale în afara directorului autorizat: acces blocat.

### B5 – SQL UNION și regex

Am creat două tabele SQLite cu date fictive și am combinat rezultatele folosind `UNION`.

Am utilizat `re.findall()` pentru identificarea codurilor de test formate din 32 de caractere hexazecimale.

Rezultat: 3 coduri identificate.

### Concluzie privind Lucrarea B

Am demonstrat local principiile SQL Injection, interogărilor parametrizate, validării căilor către fișiere, operației SQL UNION și expresiilor regulate.

Exercițiile B1–B5 nu au fost executate pe DVWA/Metasploitable2, ci adaptate pentru demonstrații locale. Prin urmare, realizarea lor nu reprezintă confirmarea vulnerabilităților pe ținta cerută în laborator.