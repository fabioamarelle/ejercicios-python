def penjat():
    # Inicialitza variables
    lletresFallades = []
    vides = 6
    jocAcaba = False
    nomJ1, nomJ2 = "",""

    print("\n" * 30)
    print("Activitat 6: Joc del penjat")
    print("Fabio Amarelle Rodrigues")
    print()

    # Pregunta els noms als usuaris, no permet variables buides
    while nomJ1 == "":
        nomJ1 = input("Introdueix el nom del jugador que triarà la paraula: ")
    while nomJ2 == "":
        nomJ2 = input("Introdueix el nom del jugador que endivinarà la paraula: ")

    # Executa tot el codi fins que un usuari guanya
    paraula, paraulaOculta = obtenir_paraula(nomJ1)
    while not jocAcaba:
        intentLletra = obtenirLletra(nomJ2)
        paraulaOculta, vides, lletresFallades = comprovarLletra(paraula, paraulaOculta, intentLletra, vides,lletresFallades)
        mostrar_estat(paraulaOculta,lletresFallades,vides)
        jocAcaba = jocAcabat(paraulaOculta, vides, nomJ1, nomJ2, paraula)

    tornarAJugar = input("Vols tornar a jugar? (S/N): ").upper()
    if tornarAJugar == "S":
        penjat()
    elif tornarAJugar == "N":
        exit()

def obtenir_paraula(nomJ1):
    from getpass import getpass
    # L'usuari tria la paraula oculta
    while True:
        paraula = getpass(f"{nomJ1}, tria la paraula oculta: ").lower()
        # Valida que sigui una única paraula (revisa espais) 
        if " " in list(paraula):
            print("Introdueix només una paraula.")
        # Altres comprovacions (espai en blanc, longitud, símbols)
        elif paraula == "" or len(paraula) == 1 or not paraula.isalpha():
            print("Introdueix una paraula.")
        else: break 

    # Tradueix la paraula a guions baixos
    paraulaOculta = ""
    for i in paraula:
        paraulaOculta += "_"
    return paraula,list(paraulaOculta)

def mostrar_estat(paraulaOculta,lletresFallades,vides):
    print(f"Paraula oculta: {' '.join(paraulaOculta).upper()}")
    print(f"Lletres fallades: {', '.join(lletresFallades).upper()}")
    print(f"Nombre de vides: {vides}")
    dibuixar_penjat(vides)

def obtenirLletra(nomJ2):
    import string
    intentLletra = input(f"{nomJ2}, introdueix una lletra:").lower()
    while intentLletra not in (string.ascii_letters+"ñçáàéèíìïóòúùü") or len(intentLletra) != 1:
        intentLletra = input(f"{nomJ2}, introdueix una lletra:").lower()
    return intentLletra

def comprovarLletra(paraula, paraulaOculta, intentLletra, vides,lletresFallades):
    llistaPosicions = []
    if intentLletra in lletresFallades or intentLletra in list(paraulaOculta):
        print("Ja has introduït aquesta lletra.")
    else:
        cercaParaula = list(paraula)
        # Troba totes les posicions de la lletra a la paraula
        for i in range(paraula.count(intentLletra)):
            # Troba l'index, l'afegeix a una llista
            posicio = cercaParaula.index(intentLletra)
            llistaPosicions.append(posicio)
            # Reemplaça la lletra ja trobada per "*"
            cercaParaula[posicio] = "*"

        # Reemplaça els "_" trobats per les seves lletres
        for i in llistaPosicions:
            paraulaOculta[i] = intentLletra
        # Resta una vida si no hi ha cap lletra
        if llistaPosicions == []: 
            vides -= 1
            lletresFallades.append(intentLletra)  
    return paraulaOculta, vides,lletresFallades

def jocAcabat(paraulaOculta, vides, nomJ1, nomJ2, paraula):
    if not "_" in list(paraulaOculta):
        print(f"{nomJ2} ha guanyat.")
        print(f"La paraula oculta era: {paraula.capitalize()}")
        return True
    elif vides == 0:
        print(f"{nomJ2} s'ha quedat sense vides, {nomJ1} ha guanyat.")
        print(f"La paraula oculta era: {paraula.capitalize()}")
        return True

def dibuixar_penjat(vides):
    print(" ------")
    print(" |    |")

    # Cap
    if vides == 0:      print(" |        ")
    else:               print(" |    o   ")
    
    # Cos
    if vides >= 4:      print(" |   /|\\ ")  # El símbol \ dóna error si es fica sol.
    elif vides == 3:    print(" |   /|   ")
    elif vides == 2:    print(" |    |   ")
    else:               print(" |        ")

    # Cames
    if vides == 6:      print(" |   / \\ ")
    elif vides == 5:    print(" |   /    ")
    else:               print(" |        ")
    
    print(" |    ")
    print(" |    ")
    print("---   ")

penjat()