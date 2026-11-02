# Laboratorul 6

Decoder, analiză forensic și steganografie pe probele proprii. Vezi [raportul](raport.md) pentru rezultatele lucrării.

- `arsenal/forensics/`: programele și fișa JSON.
- `probe/pregateste.py`: generatorul datelor de laborator.
- `teste/test_decode.py`: cele șapte teste.

Din rădăcina depozitului, execută:

```powershell
cd lab6
python -m pip install pillow pytest
python probe/pregateste.py
python -m arsenal.forensics.decode probe/mesaj.txt --fisier
python -m arsenal.forensics.forensics
python -m arsenal.forensics.stego
python -m pytest -q teste/test_decode.py
```

Generatorul creează probele în `probe/`, decoderul scrie fișa în `arsenal/forensics/fisa.json`, iar programul LSB creează `stego.png` în folderul `lab6/`.
