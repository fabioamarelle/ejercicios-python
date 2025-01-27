primeraA = False
caractersFrase = 0

frase = input("Introdueix una frase: ")

for lletra in frase:
    if primeraA == True:        # Si ja ha trobat una A, suma 1 al comptador en cada caràcter, independentment de la lletra
        caractersFrase += 1

    if lletra == "a" or lletra == "A":  # Si es detecta una A, canvia primeraA a True
        primeraA = True

print(f"Hi ha {caractersFrase} caràcters després de la primera A a la frase.")