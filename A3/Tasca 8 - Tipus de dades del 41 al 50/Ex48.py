cadena = input("Introdueix una cadena de text: ")

for lletra in cadena:
    if lletra.isupper():                    # Si és majúscula:
        print(lletra.lower(), end="")       # Imprimeix lletra minúscula

    elif lletra.islower():                  # Si és minúscula:
        print(lletra.upper(), end="")       # Imprimeix lletra majúscula

    else:                                   # Si no és majúscula ni minúscula (número):
        print(lletra, end="")               # Imprimeix