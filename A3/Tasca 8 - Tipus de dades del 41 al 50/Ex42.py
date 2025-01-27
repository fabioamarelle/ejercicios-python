cadena = input("Introdueix una cadena de text: ")
subcadena = input("Introdueix la cadena a buscar: ")
cadenaIgual = True
for i in range(1, len(subcadena)):
    if cadena[i] != subcadena[i]:
        cadenaIgual = False

if cadenaIgual:
    print(f"{cadena} comença per {subcadena}.")
else:
    print(f"{cadena} no comença per {subcadena}.")
