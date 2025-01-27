cadena = input("Introdueix una cadena de text: ")
comptador = len(cadena)
cadenaInvertida = ""

for lletra in cadena:
    cadenaInvertida += cadena[comptador-1]
    comptador -= 1

if cadena.lower() == cadenaInvertida.lower():
    print(f"{cadena} és un palíndrom")