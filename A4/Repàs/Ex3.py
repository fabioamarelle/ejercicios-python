import random, os

matriu = [[],[],[],[]]
for fila in range(len(matriu)):
    for columna in range(len(matriu)):
        matriu[fila].append([])




x = random.randint(0,len(matriu)-1)
y = random.randint(0,len(matriu[x])-1)


matriu[y][x] = "X"

for llista in matriu:
    print(*llista)

moviment = ""

while moviment != "S":
    moviment = input("Moviment: ").upper()
    os.system("cls")

    if moviment == "W":
        try:
            if y - 1 < 0:
                raise IndexError
            matriu[y-1][x] = "X"
            matriu[y][x] = []
            y -= 1
        except IndexError:
            print("Fora del rang")

    if moviment == "D":
        try:
            matriu[y][x+1] = "X"
            matriu[y][x] = []
            x += 1
        except IndexError:
            print("Fora del rang")

    if moviment == "A":
        try:
            if x - 1 < 0:
                raise IndexError
            matriu[y][x-1] = "X"
            matriu[y][x] = []
            x -= 1
        except IndexError:
            print("Fora del rang")
    
    for llista in matriu:
        print(*llista)