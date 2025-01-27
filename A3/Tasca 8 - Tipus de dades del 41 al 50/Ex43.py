cadena = input("Introdueix una cadena de text: ")

while True:
    subcadena = input("Introdueix el caràcter a buscar: ")
    if len(subcadena) != 1:                  # Si subcadena no té exactament un caràcter:
        print("Format incorrecte, introdueix un sol caràcter")
    else: break

nVegades = cadena.lower().count(subcadena.lower())

# nVegades = cadena.count(subcadena)        No distingueix entre majúscules i minúscules

print(f"{subcadena} apareix {nVegades} vegades en {cadena}.")