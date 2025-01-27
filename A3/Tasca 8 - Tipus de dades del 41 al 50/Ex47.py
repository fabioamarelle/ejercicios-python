cadena = input("Introdueix una cadena de text: ")

while True:
    caracter1 = input("Introdueix el caràcter a reemplaçar: ")
    if len(caracter1) != 1:
        print("Format incorrecte, introdueix un sol caràcter")
    else: break

while True:
    caracter2 = input("Introdueix el caràcter pel qual es reemplaçarà: ")
    if len(caracter2) != 1:
        print("Format incorrecte, introdueix un sol caràcter")
    else: break



for lletra in cadena:
    if lletra == caracter1:                 # Si la lletra és igual a la variable caracter1:
        print(caracter2, end="")            # En comptes d'imprimir aquesta lletra, imprimeix la variable caracter2
    else:
        print(lletra, end="")