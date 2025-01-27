lletraL = False
numLA = 0 
frase = input("Introdueix una frase: ")

for lletra in frase:
    if lletra == "L":
        lletraL = True          # Hi ha una lletra "L" abans
    elif lletra == "A":
        if lletraL == True:     # Si hi ha una lletra "L" abans de la "A":
            numLA += 1          # Afegeix 1 al comptador 
    else:                       # Si després de la lletra "L" no hi ha una "A":
        lletraL = False         # No hi ha una lletra "L" abans

print(numLA)