numB = 0
numC = 0

frase = input("Introdueix una frase: ")

for lletra in frase:
    if lletra == "b" or lletra == "B":      # Si es troba una B, suma 1 al comptador numB
        numB += 1
    elif lletra == "c" or lletra == "C":    # Si es troba una C, suma 1 al comptador numC
        numC += 1

# Comparacions entre dos comptadors
if numB > numC:
    print(f"Hi ha més caràcters B que C.")
if numC > numB:
    print(f"Hi ha més caràcters C que B.")
if numB == numC:
    print(f"Hi ha els mateixos caràcters B que C.")