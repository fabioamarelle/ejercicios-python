import keyboard, os, time, random
from emoji import emojize

def iniciarJoc():
    # Genera la matriu i afegeix el jugador.
    global files, columnes, matriu, casella, personatge, obstacle
    os.system("cls")
    jugador = emojize(":elf:")
    obstacle = emojize(":deciduous_tree:")
    tresor = emojize(":gem_stone:")
    enemic = emojize(":dragon:")
    casella = "ㅤ"
    
    nom = ""
    while nom == "":
        nom = input("Introdueix el teu nom: ")

    personatge = {
                    "Nom": nom,
                    "Classe": "Guerrer",
                    "Nivell": 5,
                    "Vida": 100,
                    "Inventari": []
                  }

    matriu, files, columnes = crearMatriu()
    
    # Genera el jugador en una posició aleatòria
    generarObjecte(jugador,files*columnes)  # 1
    generarObjecte(tresor, 20)              # 1/20 
    generarObjecte(enemic, 20)              # 1/20
    
    return jugador, casella, obstacle, tresor, enemic, matriu, files, columnes

def crearMatriu():
    # Tria les mides de la matriu
    while True:
        midaMatriu = input("Introdueix la mida del mapa (ex: 5x5): ")
        try:
            files, columnes = midaMatriu.split("x")
            files = int(files)
            columnes = int(columnes)
            if files >= 5 and columnes >= 5:
                if files <= 40 and columnes <= 40:
                    break
                else: print("La mida màxima és 40x40.")
            else: print("La mida mínima és 5x5.")
        except ValueError:
            print("Format incorrecte. El format ha de ser 'númeroXnúmero'.")
    
    # Si les dimensions són parelles donarà problemes en la generació de camins. Es suma 1 a les files i/o columnes si són parelles.
    if files % 2 == 0: files += 1
    if columnes % 2 == 0: columnes += 1

    matriu = []
    for i in range(columnes):
        matriu.append(list(obstacle * files))  # Crea una matriu d'obstacles
    
    def crearCamins(x, y):
        direccions = [(0, 2), (0, -2), (2, 0), (-2, 0)]  # Possibles direccions, es mou dues caselles per cada moviment

        # Tria una direcció al atzar
        random.shuffle(direccions)
        for dx, dy in direccions:  # Tria la primera direcció
            nouX, nouY = x + dx, y + dy 
            
            # "Si la posició està dins de la matriu i és un obstacle"
            if 0 <= nouY < columnes and 0 <= nouX < files and matriu[nouY][nouX] == obstacle:
                matriu[y + (dy // 2)][x + (dx // 2)] = "ㅤ"  # Crea un camí a la primera posició
                matriu[nouY][nouX] = "ㅤ"  # Crea un camí a la segona posició
                crearCamins(nouX, nouY)  # Torna a cridar la funció, aquesta vegada des de la nova posició. La funció pararà quan no pugui crear camins en cap direcció.

    crearCamins(1, 1)   # Comença des de 1,1  
    return matriu, files, columnes

def generarObjecte(objecte, proporcio):
    for i in range(int(round((files*columnes/proporcio),0))):
        while True:
            fila = filaAleatoria(files)
            columna = columnaAleatoria(columnes)
            if matriu[columna][fila] == casella:
                matriu[columna][fila] = objecte
                break

def filaAleatoria(files):
    return random.randint(0,files-1)    # Solució a IndexError.

def columnaAleatoria(columnes):
    return random.randint(0,columnes-1)

def trobarJugador():
    # Es necessita la posició inicial del jugador abans de moure'l.
    i = 0
    # Busca l'icona del jugador a la matriu i dona les coordenades.
    for llista in matriu:
        if jugador in llista:
            x = llista
            break
        else: i += 1
    coordenadaX = x.index(jugador)
    coordenadaY = i

    for llista in matriu: print(*llista)
    return coordenadaY, coordenadaX

def mostrarEstat():
    print(f"{personatge['Nom']} - ❤️  {personatge['Vida']}  | 🧪 - [P] ")
    print("─" * files*3)
    numPocions = personatge["Inventari"].count(emojize(":test_tube:"))
    numEscuts = personatge["Inventari"].count(emojize(":shield:"))
    numDestrals = personatge["Inventari"].count(emojize(":axe:"))
    numEspases = personatge["Inventari"].count(emojize(":dagger:"))
    print(f"🧰 : 🧪 x{numPocions}, 🛡️  x{numEscuts}, 🪓 x{numDestrals}, 🗡️  x{numEspases}")
    print("─" * files*3)
    for llista in matriu:
        print(*llista)

def llegirTecla():
    # Funciona junt amb moureJugador(). Llegeix tecles i dona les posicions a aquesta funció.
    tecla = keyboard.read_key()
    os.system("cls")
    if tecla == "w":
        moureJugador(-1, 0)
    elif tecla == "a":
        moureJugador(0, -1)
    elif tecla == "s":
        moureJugador(1, 0)
    elif tecla == "d":
        moureJugador(0, 1)
    elif tecla == "p":
        utilitzarPocio()
    mostrarEstat()
    time.sleep(0.25)

def moureJugador(dy, dx):
    # Funciona junt amb llegirTecla(). Rep una posició on intentar moure el jugador, revisa si compleix les condicions, i mou el jugador.
    global coordenadaY, coordenadaX  # Alternativa a fer un return i donar variables
    matriu[coordenadaY][coordenadaX] = casella
    
    if 0 <= (coordenadaY + dy) < len(matriu) and 0 <= (coordenadaX + dx) < len(matriu[0]):
        if matriu[coordenadaY + dy][coordenadaX + dx] == obstacle:
            if emojize(":axe:") in personatge["Inventari"]:
                personatge["Inventari"].remove(emojize(":axe:"))
                coordenadaY += dy
                coordenadaX += dx
        else: 
                coordenadaY += dy
                coordenadaX += dx
    if matriu[coordenadaY][coordenadaX] == tresor:
        obtenirTresor()
    elif matriu[coordenadaY][coordenadaX] == enemic:
        trobarDrac()

    matriu[coordenadaY][coordenadaX] = jugador

def obtenirTresor():
    possiblesRecompenses =[
        ["Poció", "Destral", "Escut", "Espasa"],
        [emojize(":test_tube:"), emojize(":axe:"), emojize(":shield:"),  emojize(":dagger:")],
    ]
    recompensa = random.randint(0,100)
    if 0 <= (recompensa) <= 15:
        recompensa = possiblesRecompenses[1][0]
        print(f"Has trobat una poció.")
    elif 16 <= (recompensa) <= 60:
        recompensa = possiblesRecompenses[1][1]
        print(f"Has trobat una destral.")
    elif 61 <= (recompensa) <= 85:
        recompensa = possiblesRecompenses[1][2]
        print(f"Has trobat un escut.")
    elif 86 <= (recompensa) <= 100:
        recompensa = possiblesRecompenses[1][3]
        print(f"Has trobat una espasa.")

    personatge["Inventari"].append(recompensa)

def trobarDrac():
    # Si el jugador té 🛡️ i 🗡️, no perdrà vida
    if emojize(":dagger:") in personatge["Inventari"] and emojize(":shield:") in personatge["Inventari"]:
        personatge["Inventari"].remove(emojize(":dagger:"))
        personatge["Inventari"].remove(emojize(":shield:"))

    # Si el jugador té 🗡️, només perdrà 25 punts de vida
    elif emojize(":dagger:") in personatge["Inventari"]:
        if personatge["Vida"] - 25 < 0:
            personatge["Vida"] = 0
        else:
            personatge["Vida"] -= 25
        personatge["Inventari"].remove(emojize(":dagger:"))

    # Si el jugador té 🛡️, només perdrà 25 punts de vida
    elif emojize(":shield:") in personatge["Inventari"]:
        if personatge["Vida"] - 25 < 0:
            personatge["Vida"] = 0
        else:
            personatge["Vida"] -= 25
        personatge["Inventari"].remove(emojize(":shield:"))

    # Si no té res, perd 40 punts de vida
    else: 
        if personatge["Vida"] - 40 < 0:
            personatge["Vida"] = 0
        else:
            personatge["Vida"] -= 40

def utilitzarPocio():
    if emojize(":test_tube:") in personatge["Inventari"]:
        if personatge["Vida"] + 30 > 100:
            personatge["Vida"] = 100
        else: personatge["Vida"] += 30
        personatge["Inventari"].remove(emojize(":test_tube:"))
    else: print("No tens pocions.")

def jocAcabat():
    quedenTresors = False
    if personatge["Vida"] <= 0:
        print(f"{personatge['Nom']} s'ha quedat sense vida.")
        exit()
    for llista in matriu:
        if tresor in llista:
            quedenTresors = True
            break
    if not quedenTresors:
        print(f"Has trobat tots els tresors. Has guanyat!")
        exit()

def pantallaInicial():
    os.system("cls")
    print("Activitat 7: Joc de rol")
    print("─" * 25)
    print("Fabio Amarelle Rodrigues")
    print("\n"*3)
    print("Prém Enter per a començar")
    input()

pantallaInicial()

jugador, casella, obstacle, tresor, enemic, matriu, files, columnes = iniciarJoc()
coordenadaY, coordenadaX = trobarJugador()

while True:
    llegirTecla()
    jocAcabat()