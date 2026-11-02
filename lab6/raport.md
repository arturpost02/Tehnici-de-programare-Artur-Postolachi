# Laboratorul nr. 6 – Informații invizibile: forensics și steganografie

**Student:** Artur Postolachi<br>
**Disciplina:** Tehnici de programare · UTM · Securitate informațională

## Scop
Realizarea unui decoder universal și a unor unelte Python de analiză forensic pe fișiere generate special pentru laborator. Nu sunt analizate fișierele altor persoane.

## Lucrarea A (A1–A7)
- **A1:** Textul „Salut” a fost convertit în octeți și reprezentare hexazecimală prin `encode()`, `hex()` și `bytes.fromhex()`.
- **A2:** `ghici_strat()` identifică URL, HEX și Base64 după structură.
- **A3:** `desfa()` decodează separat fiecare codare.
- **A4:** `decodare_straturi()` desface repetat Base64 → Base64 → HEX și obține `FLAG{straturi_de_encoding}`.
- **A5:** Prin încercarea celor 256 de chei XOR a rezultat cheia **128 (0x80)** și mesajul `Un singur octet tine tot secretul... gaseste-l! FLAG{xor_un_octet}`.
- **A6:** Hash-urile din probă sunt MD5 (32 caractere hex), iar pentru primul hash parola găsită în dicționar este `password`.
- **A7:** Decoderul primește intrarea în terminal prin `argparse` și scrie `arsenal/forensics/fisa.json`. Testul `test_base64` verifică decodarea `U2FsdXQ=` → `Salut`.

## Lucrarea B (B1–B6)
- **B1:** Semnături binare: `foto.jpg` = JPEG, `ascuns.png` = PNG.
- **B2:** Expresia regulată pentru secvențe imprimabile identifică indicii textuale din fișierul PNG.
- **B3:** Metadatele EXIF generate: producător Apple, model iPhone 13, data 2026-09-14 10:30:00. Coordonate aproximative: **47.016667 N, 28.857500 E**.
- **B4:** În coada fișierului `ascuns.png` este o arhivă ZIP. `secret.txt` conține `FLAG{ascuns_prin_carving}`.
- **B5:** Un mesaj este introdus în cel mai puțin semnificativ bit al canalelor RGB, apoi imaginea este salvată fără pierderi în `stego.png`.
- **B6:** Reconstituirea octeților până la terminatorul nul dezvăluie `FLAG{ascuns_in_pixeli}`.

## Testare și reproducere
Pe copia locală a proiectului, `pytest` a finalizat cu **7 teste trecute**. Pentru regenerarea probelor și a imaginii LSB în clona GitHub:

```powershell
python -m pip install pillow pytest
python probe/pregateste.py
python -m arsenal.forensics.decode probe/mesaj.txt --fisier
python -m arsenal.forensics.forensics
python -m arsenal.forensics.stego
python -m pytest -q teste/test_decode.py
```

Fișierele binare de probă și `stego.png` sunt produse local de scripturi; dacă trebuie predate pe GitHub, trebuie și adăugate prin `git add`, `git commit`, `git push`. Rezultatele indicate mai sus sunt pentru datele definite de generator.
