# Laboratorul 8

## Lucrarea A

`salut.py` este programul creat pentru exercițiile Git:

```powershell
cd lab8
python salut.py
```

Exercițiile primei părți au fost realizate în depozitul de curs. Al doilea depozit, creat de pe calculator pentru A10, este [exercitiu-2](https://github.com/arturpost02/exercitiu-2).

Regulile comune de ignorare sunt în fișierul `.gitignore` din rădăcina depozitului și se aplică și subfolderelor.

## Lucrarea B

Folderul `depanare/` conține `inventar.py`, `tinte.json` și raportul final `raport_inventar.json`.

Din folderul `lab8/`:

```powershell
cd depanare
python inventar.py tinte.json --prag 1000
python inventar.py tinte.json
```

Istoricul păstrează versiunea stricată, câte un commit pentru fiecare dintre cele zece reparații și commit-ul raportului final. Mutarea în `lab8/` a fost făcută ulterior, fără rescrierea istoricului.

Pentru a urmări istoricul fișierului mutat, din rădăcina depozitului:

```powershell
git log --follow --oneline -- lab8/depanare/inventar.py
```

La realizarea lucrării a fost folosit ChatGPT pentru îndrumare la depanare și la organizarea depozitului.
