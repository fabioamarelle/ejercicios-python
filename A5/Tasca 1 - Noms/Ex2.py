import os
from Ex1 import validar

filename = "/fitxers/noms.txt"
path = os.getcwd()
llista = []

with open(path+filename) as txt:
    lines = txt.readlines()

    # Per cada línia al fitxer de text, crea un diccionari i l'afegeix a la llista
    for line in lines:
        dict = {}
        persona = line.split(" ")
        dict["nom"] = persona[0]
        dict["cognom"] = persona[1]

        llista.append(dict)

for diccionari in llista:
    print(diccionari)


# Afegir un usuari (diccionari a str)
print("Afegint un nou usuari")

nouUsuari = {}
nouUsuari["nom"] = validar(input("Introdueix un nom: "), "nom")
nouUsuari["cognom"] = validar(input("Introdueix un cognom: "), "cognom")

llista.append(nouUsuari)

with open(path+filename, "w") as txt:
    for usuari in llista:
        txt.write(f"{usuari["nom"]} {usuari["cognom"]} \n")