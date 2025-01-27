import os, random, time, string

def main():
    os.system("cls")
    nomJ1, nomJ2, puntsJ1, puntsJ2, tornActual, jocAcabat = iniciarJoc()
    cartes, cartesOcultes = generarCartes()
    mostrarCartes(cartes)

    while not jocAcabat:
        primeraCarta, segonaCarta, cartesOcultesCopia = demanarCartes(cartes,cartesOcultes, tornActual, puntsJ1, puntsJ2, nomJ1, nomJ2)
        cartesOcultes, tornActual, puntsJ1, puntsJ2 = revisarCartes(cartesOcultes, primeraCarta, segonaCarta, cartes, cartesOcultesCopia, tornActual, nomJ1, nomJ2, puntsJ1, puntsJ2)
        jocAcabat = jocAcaba(cartesOcultes, puntsJ1, puntsJ2, nomJ1, nomJ2)

def iniciarJoc():
    # Pregunta els noms als usuaris, no permet variables buides
    nomJ1, nomJ2 = "",""
    while nomJ1 == "":
        nomJ1 = input("Introdueix el nom del primer jugador: ")
    while nomJ2 == "":
        nomJ2 = input("Introdueix el nom del segon jugador: ")

    # Inicialitza i retorna variables
    puntsJ1, puntsJ2 = 0,0
    tornActual = nomJ1
    jocAcabat = False
    return nomJ1, nomJ2, puntsJ1, puntsJ2, tornActual, jocAcabat

def generarCartes():
    # Permet triar la quantitat de parelles que es generen
    while True:
        numCartes = input("Introdueix la quantitat de parelles a generar: ")
        try:
            numCartes = int(numCartes)
            if 2 <= numCartes <= 26:
                break
            else: print("S'ha d'introduir un nombre entre 2 i 26.")
        except ValueError:
            print("Introdueix un nombre.")

    # Defineix les cartes, repetides dues vegades, i les barreja
    cartes = list(string.ascii_uppercase)[0:numCartes] * 2
    random.shuffle(cartes) 

    # Genera les cartes ocultes
    cartesOcultes = list("▯" * len(cartes))
    return cartes, cartesOcultes

def mostrarCartes(cartes):
    # Calcula la primera i la segona meitat de les cartes, i les mostra
    print(*cartes[0:int(len(cartes)/2)])
    print(*cartes[(int(len(cartes)/2)):int(len(cartes))])
    # Mostra les cartes ≈5 segons, esborra la terminal
    time.sleep(5)
    os.system('cls')

def demanarCartes(cartes, cartesOcultes, tornActual, puntsJ1, puntsJ2, nomJ1, nomJ2):
    # Demana les cartes, revisa que estigui entre 
    cartesOcultesCopia = list(cartesOcultes)

    # Primera carta
    os.system('cls')
    cartesActualitzades(cartesOcultes, cartes, puntsJ1, puntsJ2, nomJ1, nomJ2)
    while True:
        primeraCarta = input(f"{tornActual}, selecciona una carta: ")
        try:
            primeraCarta = int(primeraCarta)
            if 0 < primeraCarta <= len(cartes):
                if cartesOcultes[primeraCarta-1] == "▯":
                    break
                else: print("Aquesta carta ja està revelada")
            else: print(f"Introdueix un número entre 1 i {len(cartes)}.")
        except ValueError:
            print("Introdueix un número.")
        
    primeraCarta -= 1
    cartesOcultes[primeraCarta] = cartes[primeraCarta]

    # Segona carta
    os.system('cls')
    cartesActualitzades(cartesOcultes, cartes, puntsJ1, puntsJ2, nomJ1, nomJ2)
    while True:
        segonaCarta = input(f"{tornActual}, selecciona una carta: ")
        try:
            segonaCarta = int(segonaCarta)
            if 0 < segonaCarta <= len(cartes):
                if cartesOcultes[segonaCarta-1] == "▯":
                    break
                else: print("Aquesta carta ja està revelada")
            else: print(f"Introdueix un número entre 1 i {len(cartes)}.")
        except ValueError:
            print("Introdueix un número.")
    segonaCarta -= 1
    cartesOcultes[segonaCarta] = cartes[segonaCarta]
    return primeraCarta, segonaCarta, cartesOcultesCopia

def revisarCartes(cartesOcultes, primeraCarta, segonaCarta, cartes, cartesOcultesCopia, tornActual, nomJ1, nomJ2, puntsJ1, puntsJ2):
    # Revisa si les cartes són iguals
    os.system('cls')
    cartesActualitzades(cartesOcultes, cartes, puntsJ1, puntsJ2, nomJ1, nomJ2)
    if cartes[primeraCarta] == cartes[segonaCarta]:
        print("Cartes iguals")
        if tornActual == nomJ1:
            puntsJ1 += 1
        elif tornActual == nomJ2:
            puntsJ2 += 1
        time.sleep(2)

        return cartesOcultes, tornActual, puntsJ1, puntsJ2
    
    # Revisa si les cartes són diferents
    elif cartes[primeraCarta] != cartes[segonaCarta]:
        print("Cartes diferents")
        if tornActual == nomJ1:
            tornActual = nomJ2
        elif tornActual == nomJ2:
            tornActual = nomJ1
        time.sleep(2)
        return cartesOcultesCopia, tornActual, puntsJ1, puntsJ2

def cartesActualitzades(cartesOcultes, cartes, puntsJ1, puntsJ2, nomJ1, nomJ2):
    punts = f"{nomJ1}: {puntsJ1} ─ {nomJ2}: {puntsJ2}"
    print(f"{punts.center(len(cartes))}")
    print("─" * len(cartes))
    print(*cartesOcultes[0:int(len(cartes)/2)])
    print(*cartesOcultes[(int(len(cartes)/2)):int(len(cartes))])
    print("─" * len(cartes))

def jocAcaba(cartesOcultes, puntsJ1, puntsJ2, nomJ1, nomJ2):
    if not "▯" in cartesOcultes:
        print("Ha acabat el joc.")
        if puntsJ1 > puntsJ2:
            print(f"{nomJ1} ha guanyat.")
        elif puntsJ1 < puntsJ2:
            print(f"{nomJ2} ha guanyat.")
        else: 
            print("Hi ha un empat.")
        return True

main()
