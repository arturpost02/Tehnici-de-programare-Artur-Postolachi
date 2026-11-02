import sqlite3

# Cream o baza de date temporara
db = sqlite3.connect(":memory:")

# Cream un tabel
db.execute("CREATE TABLE u(nume, parola)")

# Introducem un utilizator de test
db.execute(
    "INSERT INTO u VALUES (?, ?)",
    ("artur", "x")
)

# Interogare SQL parametrizata
q = "SELECT * FROM u WHERE nume = ?"

# Cautam un utilizator existent
rezultat1 = db.execute(q, ("artur",)).fetchall()
print("Utilizator existent:", rezultat1)

# Cautam un utilizator inexistent
rezultat2 = db.execute(q, ("necunoscut",)).fetchall()
print("Utilizator inexistent:", rezultat2)


# B6 - Verificarea protectiei impotriva SQL Injection

intrare_test = "' OR '1'='1"

rezultat3 = db.execute(
    q,
    (intrare_test,)
).fetchall()

print("Test protectie SQL Injection:", rezultat3)

db.close()
