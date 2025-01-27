text = ""
while text == "":
    text = input("Introdueix un text: ")

# Demana el primer caràcter, valida la longitud
while True:
    caracter1 = input("Introdueix el caràcter que vols substituir: ")
    if len(caracter1) == 1:
        break
    else:
        print("Introdueix un caràcter.")

# Demana el segon caràcter, valida la longitud
while True:
    caracter2 = input("Introdueix el caràcter pel qual substituir: ")
    if len(caracter2) == 1:
        break
    else:
        print("Introdueix un caràcter.")

print("Frase: ",end="")


for lletra in text:                            # Revisa cada lletra
    if lletra.lower() == caracter1.lower():       # Si la lletra és igual a caracter1:
        try:
            int(lletra)
            print(caracter2, end="")
        except ValueError:
            if lletra.lower() == lletra:                 # Si la lletra era minúscula:
                print(caracter2.lower(),end="")             # Imprimeix caracter2 (minúscula)
            if lletra.upper() == lletra:                 # Si la lletra era majúscula:
                print(caracter2.upper(),end="")             # Imprimeix caracter2 (majúscula)
    else:
        print(lletra, end="")