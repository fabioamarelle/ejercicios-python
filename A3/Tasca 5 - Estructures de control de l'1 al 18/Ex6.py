lletra = str(input("Introdueix una lletra: "))
if not len(lletra) == 1:                # len() retorna el nombre de lletres
    print("Introdueix només una lletra.") 
elif str.isupper(lletra):       # isupper() comprova si tots els caràcters estan en majúscula
    print("La lletra és majúscula.")
else:
    print("La lletra és minúscula.")