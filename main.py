"""Demonstrație pentru exercițiul «Verificatorul stării site-urilor»."""
from urllib.parse import urlparse

from checker import (
    SITES,
    build_url,
    is_https,
    show_response,
    check_site,
    scan_sites,
    check_headers,
    retry_check,
)


# Partea 1: funcții ajutătoare - două exemple pentru fiecare.
print("\n=== Partea 1: Funcții ===")
host = urlparse(SITES[0]).hostname
print("build_url fără /:", build_url(host, "login"))
print("build_url cu /:", build_url(host, "/login"))
print("is_https HTTPS:", is_https(SITES[0]))
print("is_https HTTP:", is_https(SITES[9]))

# Partea 2: status și Content-Type.
print("\n=== Partea 2: Trimiterea unei cereri ===")
print("show_response, site obișnuit:", SITES[0])
show_response(SITES[0])
print("show_response, eroare 404:", SITES[6])
show_response(SITES[6])

# Partea 3: teste pe TOATE adresele din lista SITES.
print("\n=== Partea 3: Verificator reutilizabil ===")
for site in SITES:
    print("check_site:", site, "->", check_site(site))

# Partea 4: scanare, sortare și numărare.
print("\n=== Partea 4: Verificarea mai multor site-uri ===")
scan_sites()

# Partea 5: antete prezente, majuscule/minuscule și site indisponibil.
print("\n=== Partea 5: Audit de securitate ===")
print("check_headers, două antete:", check_headers(SITES[10]))
print("check_headers, antet cu litere mici:", check_headers(SITES[11]))
print("check_headers, site invalid:", check_headers(SITES[9]))

# Partea 6: răspuns 200, 404, 500 și site indisponibil.
print("\n=== Partea 6: Încercări repetate ===")
print("retry_check 200:", retry_check(SITES[3]))
print("retry_check 404:", retry_check(SITES[6]))
print("retry_check 500:", retry_check(SITES[7]))
print("retry_check 500 (două încercări):", retry_check(SITES[7], attempts=2))
print("retry_check site invalid:", retry_check(SITES[9]))
