
from pathlib import Path
from tempfile import TemporaryDirectory

# B4 - Validarea sigura a cailor catre fisiere

with TemporaryDirectory() as director:
    baza = Path(director).resolve()

    # Cream un fisier fictiv de laborator
    (baza / "mesaj.txt").write_text(
        "Laboratorul 5 - fisier de test",
        encoding="utf-8"
    )

    def citeste_sigur(nume):
        cale = (baza / nume).resolve()

        # Permitem doar fisiere din directorul autorizat
        if not cale.is_relative_to(baza):
            return "Acces blocat: cale nepermisa"

        if not cale.is_file():
            return "Fisierul nu exista"

        return cale.read_text(encoding="utf-8")

    print("--- B4: PROTECTIA FISIERELOR ---")

    print("Test 1:", citeste_sigur("mesaj.txt"))
    print("Test 2:", citeste_sigur("inexistent.txt"))
    print("Test 3:", citeste_sigur("../altceva.txt"))
