from arsenal.web.client import cere

# B1 - Cerere HTTP normala
url = "http://192.168.56.101:8080/"

normal = cere(
    url,
    params={"id": "1", "Submit": "Submit"}
)

print("--- B1: CERERE NORMALA ---")
print("URL:", normal.url)
print("Cod HTTP:", normal.status_code)
print("Lungime raspuns:", len(normal.content), "octeti")
print("Continut raspuns:")
print(normal.text)

# B2 - Compararea raspunsurilor HTTP

print("\n--- COMPARAREA RASPUNSURILOR ---")

url = "http://192.168.56.101:8080/"

raspuns1 = cere(url, params={"id": "1"})
raspuns2 = cere(url, params={"id": "2"})

print("Raspuns ID 1:", len(raspuns1.content), "octeti")
print("Raspuns ID 2:", len(raspuns2.content), "octeti")

if raspuns1.text == raspuns2.text:
    print("Raspunsurile sunt identice")
else:
    print("Raspunsurile sunt diferite")
