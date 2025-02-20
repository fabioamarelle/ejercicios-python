import os, random, time, string, copy

def generarCartes():
    while True:
        mida = input("Selecciona la mida de la matriu: ")
        try:
            mida = int(mida)
            if mida > 10:
                print(f"La mida màxima és 10.")
            elif mida % 2 == 0 :
                numCartes = mida * mida
                break
            else: print(f"Amb un tauler {mida}x{mida}, el nombre de cartes seria imparell i no es podrien formar parelles.")
        except ValueError:
            print("Introdueix un nombre.")
    
    numParelles = int(numCartes / 2)
    
    cartes = (list(reversed(string.ascii_letters)))[0:((numParelles))] * 2
    random.shuffle(cartes)

    # Divideix la llista en parts iguals i la converteix a una matriu
    matriu = []
    step = int((numCartes)**(1/2))
    for i in range(0, numCartes, step):
        # Utilitza la funcionalitat step de range per a crear matrius d'una mida específica.
        # Per a step = 4: A la primera iteració: 0:4 (0,1,2,3), a la segona: 4:8 (5,6,7,8)
        print(i)
        print(i+step)

        matriu.append(cartes[i:(i+step)])   

    # Converteix la matriu al símbol "▯"
    matriuOculta = []
    step = int((numCartes)**(1/2))
    for i in range(0, numCartes, step):
        matriuOculta.append(list("▯"*step))

    return matriu, matriuOculta

def demanarCartes(matriu, matriuOculta):
    matriuOcultaCopia = copy.deepcopy(matriuOculta)

    y1, x1 = demanarPosicions()
    y2, x2 = demanarPosicions()

    # Revisa si les cartes són iguals
    os.system('cls')
    mostrarMatriu(matriuOculta)

    if matriu[y1][x1] == matriu[y2][x2]:
        print("Cartes iguals")
        time.sleep(2)

        return matriuOculta
    
    # Revisa si les cartes són diferents
    else:
        print("Cartes diferents")
        time.sleep(2)
        return matriuOcultaCopia

def demanarPosicions():
    os.system('cls')
    mostrarMatriu(matriuOculta)
    while True:
        triarCarta = input(f"Selecciona una carta amb el format (x,y): ")
        try:
            x,y = triarCarta.split(",")
            x = int(x) - 1
            y = int(y) - 1
            if 0 <= y <= len(matriu) and 0 <= x <= len(matriu):
                if matriuOculta[y][x] == "▯":
                    break
                else: print("Aquesta carta ja està revelada")
            else: print(f"Introdueix valors entre 1 i {len(matriu)}.")
        except ValueError:
            print("Introdueix un número.")
        except IndexError:
            print("Posició fora de la matriu.")    

    matriuOculta[y][x] = matriu[y][x]
    return y, x

def jocAcaba(matriuOculta):
    for llista in matriuOculta:
        if "▯" in llista:
            return False
    print("Ha acabat el joc.")
    return True

def mostrarMatriu(matriuOculta):
    print("   | ", end="")
    for i in range(len(matriuOculta)):
        print(f"{i+1} ", end="")
    print()
    for i, llista in enumerate(matriuOculta):
        if i+1 >= 10:
            print(f"{i+1} | ", end="")
        else: print(f"{i+1}  | ", end="")
        print(*llista)

matriu, matriuOculta = generarCartes()
while not jocAcaba(matriuOculta):
    matriuOculta = demanarCartes(matriu,matriuOculta)