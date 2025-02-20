nomContactes = []
edatContactes = []
telContactes = []

def mostrar_menu():
    # Mostra el menú, permet a l'usuari cridar una funció
    print("[1] Afegir contactes")
    print("[2] Mostrar contactes")
    print("[3] Mostrar contactes majors de 20 anys")
    print("[4] Sortir del programa")
    opcionsMenu = input("Introdueix la opció (1,2,3,4): ")

    # Validacions per a la variable "opcionsMenu"
    while True:
        try:
            opcionsMenu = int(opcionsMenu)
            if opcionsMenu in [1,2,3,4]:
                break
            else:
                print("Opcio no trobada.")
                opcionsMenu = input("Introdueix la opció (1,2,3,4): ")
        except ValueError:
            print("Opcio no trobada.")
            opcionsMenu = input("Introdueix la opció (1,2,3,4): ")

    # Crida funcions depenent del valor de la variable "opcionsMenu"
    if opcionsMenu == 1:
        afegir_contactes()
    if opcionsMenu == 2:
        mostrar_contactes()
    if opcionsMenu == 3:
        mostrar_contactes_majors()
    if opcionsMenu == 4:
        exit()

def afegir_contactes():
    # Demana valors per al nom, edat i telèfon del nou contacte
    print("Creació d'un nou contacte")
    nom = input("Introdueix el nom: ")
    edat = input("Introdueix l'edat: ")
    # Validacions per a l'edat
    while True:
        try:
            edat = int(edat)
            break
        except ValueError:
            edat = input("Error. Introdueix l'edat: ")
    # Validacions per al telèfon
    tel = input("Introdueix el telèfon: ")
    while True:
        try:
            tel = int(tel)
            break
        except ValueError:
            edat = input("Error. Introdueix el telèfon: ")
    # Afegeix les dades a la llista, torna al menú.
    nomContactes.append(nom)
    edatContactes.append(edat)
    telContactes.append(tel)
    print("Contacte afegit.")
    print()
    mostrar_menu()

def mostrar_contactes():
    # Mostra tots els contactes de la llista
    for i in range(len(nomContactes)):
        print(f"Contacte {i+1}")
        print(f"Nom: {nomContactes[i]}")
        print(f"Edat: {edatContactes[i]}")
        print(f"Telèfon: {telContactes[i]}")
        print()

def mostrar_contactes_majors():
    # Còpia de la funció mostrar_contactes(). S'afegeix un if per verificar si el contacte és major d'edat.
    for i in range(len(nomContactes)):
        if edatContactes[i] >= 18:
            print(f"Nom: {nomContactes[i]}")
            print(f"Edat: {edatContactes[i]}")
            print(f"Telèfon: {telContactes[i]}")
            print()
    
mostrar_menu()
