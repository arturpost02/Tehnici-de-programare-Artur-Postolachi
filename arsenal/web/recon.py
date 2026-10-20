import requests
import sys
import argparse
from arsenal.web.client import cere


# A6 - Argumente din terminal

parser = argparse.ArgumentParser(
    description="Program de recunoastere web"
)

parser.add_argument("tinta", help="Adresa serverului de test")

parser.add_argument(
    "--wordlist",
    default=None,
    help="Fisier optional cu nume de directoare"
)

args = parser.parse_args()

tinta = args.tinta.rstrip("/")


r = cere(tinta)

print("Cod HTTP:", r.status_code)
print("Server:", r.headers.get("Server"))
print("X-Powered-By:", r.headers.get("X-Powered-By"))

# A2 - Citirea robots.txt

print("\n--- ROBOTS.TXT ---")

url_robots = tinta.rstrip("/") + "/robots.txt"

r_robots = cere(url_robots)

print("Cod HTTP:", r_robots.status_code)

if r_robots.status_code == 200:
    print("Continut robots.txt:")
    print(r_robots.text)

    print("\nLinii Disallow:")

    for linie in r_robots.text.splitlines():
        if linie.strip().lower().startswith("disallow:"):
            print(linie)
else:
    print("robots.txt nu a fost gasit sau nu poate fi citit.")


# A3 - Descoperirea directoarelor

print("\n--- A3: DIRECTOARE ---")


if args.wordlist:
    with open(args.wordlist, "r", encoding="utf-8") as f:
        cuvinte = [
            linie.strip()
            for linie in f
            if linie.strip()
        ]
else:
    cuvinte = [
        "admin",
        "login",
        "backup",
        "config",
        "test",
        "uploads",
        "phpmyadmin"
    ]


gasite = []

for c in cuvinte:
    url = tinta.rstrip("/") + "/" + c

    try:
        r = cere(url, timeout=10)

        if r.status_code == 200:
            gasite.append(c)
            print("Gasit:", c)

        elif r.status_code == 403:
            print("Interzis:", c)

        elif r.status_code == 404:
            print("Negasit:", c)

    except requests.RequestException as e:
        print("Eroare:", c, e)

print("Directoare gasite:", gasite)

# A4 - Extragerea linkurilor cu regex

import re

print("\n--- LINKURI GASITE ---")

r = cere(tinta, timeout=10)

linkuri = re.findall(r'href="([^"]+)"', r.text)

linkuri_unice = set(linkuri)

print("Linkuri gasite:", linkuri_unice)
print("Numar de linkuri unice:", len(linkuri_unice))

# A7 - Salvarea rezultatelor JSON

import json
from pathlib import Path

print("\n--- A7: FISA JSON ---")

# Citim informatiile serverului
raspuns = cere(tinta, timeout=10)

# Construim fisa
fisa = {
    "tinta": tinta,
    "server": raspuns.headers.get("Server"),
    "directoare": gasite,
    "linkuri": sorted(linkuri_unice)
}

# Salvam in acelasi folder cu recon.py
fisier = Path(__file__).with_name("fisa.json")

with open(fisier, "w", encoding="utf-8") as f:
    json.dump(fisa, f, indent=4, ensure_ascii=False)

print("Fisa salvata:", fisier)
print(json.dumps(fisa, indent=4, ensure_ascii=False))
