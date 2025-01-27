cadena = input("Introdueix una cadena de text: ")
subcadena = input("Introdueix una cadena a buscar: ")

if subcadena in cadena:                         # Si la subcadena apareix a la cadena:
    print(f"{subcadena} apareix a {cadena}")
else:
    print(f"{subcadena} no apareix a {cadena}")