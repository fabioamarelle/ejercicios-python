import os
filename = "\\fitxers\\noms.txt"
path = os.getcwd()
matriu = []

def afegir():
    nom = input("Introdueix el nom de l'empleat: ")
    while True:
        try:
            dni = input("Introdueix el DNI/NIE del treballador: ")
            if len(dni) == 9 and (dni[0].isalpha or dni[0].isnumeric) and dni[1:7].isnumeric() and dni[8].isalpha():    # Possibles formats: 01234567A (DNI), X0134567A (NIE)
                break
            else: print("Format del DNI/NIE incorrecte.")
        except (TypeError, IndexError):     
             print("Format del DNI/NIE incorrecte.")
    while True:
        try:
            edat = int(input("Introdueix l'edat del treballador: "))
        except ValueError: print("Valor no numèric.")
        else: break
    matriu.append([nom, dni, edat])

def mostrar():
    if matriu == []:
        print("No hi ha treballadors a mostrar.\n")
    else:
        for i,llista in enumerate(matriu):
            print(f"{"─" * 25}")
            print(f"Empleat {i+1}")
            print(f"{"─" * 25}")
            print(f"Nom: {llista[0]}")
            print(f"DNI: {llista[1]}")
            print(f"Edat: {llista[2]}")
            print(f"{"─" * 25} \n")
    input("Prèm Enter per a sortir")

def exportar():
    try:
        open(path+filename, "x")        
    except FileExistsError:
        pass
    with open(path+filename, "w") as txt:
        for llista in matriu:
            txt.write(f"{llista[0]}/{llista[1]}/{llista[2]}\n")

    print(f"Matriu exportada a {path+filename}\n")
    input("Prèm Enter per a sortir")

def importar(matriu):
    try:
        with open(path+filename) as txt:
            linies = txt.readlines()
        matriu = []
        for line in linies:
            nom, dni, edat = (line.rstrip()).split("/")
            matriu.append([nom, dni, edat])
        print("Fitxer importat.\n")
    except FileNotFoundError:
        print("No hi ha cap fitxer a importar.\n")
    input("Prèm Enter per a sortir")
    return matriu

while True:
    os.system("cls")
    print("─" * 25)
    print(" Pt3.3 - Empleats")
    print("─" * 25)
    print("[1] Afegir empleat")
    print("[2] Mostrar empleats")
    print("[3] Exportar a fitxer")
    print("[4] Importar de fitxer")
    print("[5] Sortir del programa")
    print("─" * 25)

    menu = input("Selecciona una opció: ")
    os.system("cls")

    if menu == "1":
        afegir()
    elif menu == "2":
        mostrar()
    elif menu == "3":
        exportar()
    elif menu == "4":
        matriu = importar(matriu)
    elif menu == "5":
        print("Sortint del programa.")
        exit()
    else: print("Opció invàlida")

