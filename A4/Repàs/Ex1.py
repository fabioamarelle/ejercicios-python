matriu = [[],[],[],[]]
comptador = 0
for fila in range(len(matriu)):
    for columna in range(len(matriu)):
        comptador += 1
        matriu[fila].append(comptador)

for llista in matriu:
    print(*llista)

# ------------

matriu2 = [[], [], [], []]
comptador2 = 0
for i in range(4):
    for j in range(4):
        comptador2 += 1
        matriu2[i].insert(j,comptador2)

for llista2 in matriu2:
    print(*llista2)