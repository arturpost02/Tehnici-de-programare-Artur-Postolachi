import sqlite3

# B2 - Demonstrare locala SQL Injection

# Cream baza de date temporara
db = sqlite3.connect(":memory:")

# Cream tabelul cu utilizatori fictivi
db.execute("CREATE TABLE utilizatori (id TEXT, nume TEXT)")

db.executemany(
    "INSERT INTO utilizatori VALUES (?, ?)",
    [
        ("1", "Artur"),
        ("2", "Student"),
        ("3", "Profesor")
    ]
)

# Exemplu de interogare nesigura
def cautare_nesigura(valoare):
    query = "SELECT * FROM utilizatori WHERE id = '" + valoare + "'"
    return db.execute(query).fetchall()

# Cerere normala
normal = cautare_nesigura("1")

# Intrare de test din laborator, doar pentru baza locala
intrare_test = "1' OR '1'='1"
test = cautare_nesigura(intrare_test)

# Varianta protejata
protejat = db.execute(
    "SELECT * FROM utilizatori WHERE id = ?",
    (intrare_test,)
).fetchall()

print("--- B2: SQL INJECTION ---")

print("Cerere normala:", normal)
print("Numar rezultate normale:", len(normal))

print("Cerere de test:", test)
print("Numar rezultate test:", len(test))

print("Interogare protejata:", protejat)


# B3 - Compararea mai multor intrari

print("\n--- B3: TESTARE AUTOMATA ---")

probe = [
    ("ID existent", "1"),
    ("ID inexistent", "99"),
    ("Text cu apostrof", "abc'"),
    ("Intrarea din B2", intrare_test)
]

for nume, valoare in probe:
    try:
        rezultat_nesigur = cautare_nesigura(valoare)
        nr_nesigur = len(rezultat_nesigur)
    except sqlite3.Error:
        nr_nesigur = "eroare SQL"

    rezultat_sigur = db.execute(
        "SELECT * FROM utilizatori WHERE id = ?",
        (valoare,)
    ).fetchall()

    print("Test:", nume)
    print("Interogare nesigura:", nr_nesigur)
    print("Interogare protejata:", len(rezultat_sigur))
    print("---------------------")

db.close()
