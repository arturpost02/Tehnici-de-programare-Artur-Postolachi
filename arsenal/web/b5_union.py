
import sqlite3
import re

# B5 - UNION si expresii regulate

db = sqlite3.connect(":memory:")

# Cream doua tabele
db.execute("CREATE TABLE grupa1 (nume TEXT, cod TEXT)")
db.execute("CREATE TABLE grupa2 (nume TEXT, cod TEXT)")

# Introducem date fictive
db.executemany(
    "INSERT INTO grupa1 VALUES (?, ?)",
    [
        ("Artur", "0123456789abcdef0123456789abcdef"),
        ("Student", "11111111111111111111111111111111")
    ]
)

db.execute(
    "INSERT INTO grupa2 VALUES (?, ?)",
    ("Profesor", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
)

# Combinam datele cu UNION
rezultate = db.execute("""
    SELECT nume, cod FROM grupa1
    UNION
    SELECT nume, cod FROM grupa2
    ORDER BY nume
""").fetchall()

print("--- B5: SQL UNION ---")

for nume, cod in rezultate:
    print(nume, cod)

# Transformam rezultatele in text
text = "\n".join(
    f"{nume}: {cod}" for nume, cod in rezultate
)

# Extragem codurile fictive cu regex
coduri = re.findall(r"\b[a-f0-9]{32}\b", text)

print("\n--- B5: REGEX ---")
print("Coduri gasite:", coduri)
print("Numar coduri:", len(coduri))

db.close()
