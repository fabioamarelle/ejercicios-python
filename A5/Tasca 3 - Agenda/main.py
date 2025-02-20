import re, os, json
from tabulate import tabulate

path = os.getcwd()
file = "\\fitxers\\agenda.json"

formatEmail = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
agenda = []

def afegirContacte():
    # Com és una agenda de contactes, els números de telèfon no es poden repetir
    # El nom i email es poden repetir (per a casos en els que una persona tingui dos números de telèfon diferents)

    # ID
    try:
        id = agenda[-1]["id"] + 1
    except IndexError:  # Encara no hi han usuaris, comença per 1
        id = 1 

    # Nom
    while True: 
        nom = input("Introdueix el nom de l'usuari: ").title()
        if nom.isalpha():   # Només es permeten lletres al nom.
            break
        else:
            print("El nom només pot contindre caràcters alfanumèrics.")

    # Email
    while True:
        email = input("Introdueix el correu electrònic de l'usuari: ").lower()
        if(re.search(formatEmail,email)):
            break
        else: 
            print("El format del correu electrònic és invàlid.")
    
    # Telèfon (No s'accepten telèfons repetits.)
    telefons = []
    for usuari in agenda:
        telefons.append(usuari["telefon"]) 

    while True:
        try:
            telefon = int(input("Introdueix el número de telèfon de l'usuari: "))
            if len(str(telefon)) != 9:
                print("El número de telèfon ha de tindre 9 dígits.")
            elif telefon in telefons:
                print("El número de telèfon ja està a l'agenda.")
            else: 
                telefon = str(telefon)
                break
        except ValueError:
            print("Valor no numèric.")

    # Newsletter
    newsletter = ""
    while not newsletter in [True, False]:
        newsletter = input("L'usuari vol rebre notificacions? (S/N): ").upper()
        if newsletter == "S":
            newsletter = True
        elif newsletter == "N":
            newsletter = False


    agenda.append({"id" : id, "nom" : nom, "email": email, "telefon": telefon, "newsletter": newsletter})

def mostrarAgenda():
    if agenda == []:
        print("No hi han contactes afegits.")
    else:
        format = ""
        print("─" * 25)
        print("[1] Format amb \\t")
        print("[2] Format amb el mòdul Tabulate")
        print("─" * 25)
        while format not in ["1","2"]:
            format = input("Tria una opció: ")
        os.system("cls")
        if format == "1":
            # "\t" pot tindre problemes d'estil amb valors molt llargs o curts.
            print("ID\t| Nom\t\t| Email\t\t\t| Telèfon\t| Newsletter\t|")    
            for contacte in agenda:
                mostrarContacte(contacte)

        elif format == "2":
            capcalera = agenda[0].keys()
            files =  [contacte.values() for contacte in agenda]
            print(tabulate(files, capcalera, tablefmt='fancy_grid'))

    input("\nPrèm Enter per a continuar")   
    
def mostrarContacte(contacte):
    print("─" * 100)
    
    if contacte["newsletter"]:
        newsletter = "Sí"
    else: newsletter = "No"
    
    print(f"{contacte['id']}\t| {contacte['nom']}\t\t| {contacte['email']}\t| {contacte['telefon']}\t| {newsletter}\t\t|")

def cercarContacte():
    if agenda == []:
        print("No hi han contactes afegits.")
    else:
        trobat = False
        nomACercar = input("Tria el nom de l'empleat que vols cercar: ")
        for contacte in agenda:
            if contacte["nom"].lower() == nomACercar.lower():
                if contacte["newsletter"]:
                    newsletter = "Sí"
                else: newsletter = "No"
                print("\nID\t| Nom\t\t| Email\t\t\t| Telèfon\t| Newsletter\t|")
                mostrarContacte(contacte)
                trobat = True
        if not trobat:
            print("Empleat no trobat.")
    input("\nPrèm Enter per a continuar")

def modificarContacte():
    if agenda == []:
        print("No hi han contactes afegits.")
    else:
        trobat = False
        IDACercar = int(input("Tria la ID de l'empleat que vols cercar: "))
        for contacte in agenda:
            if contacte["id"] == IDACercar:
                trobat = True
                # Nom
                nom = ""
                while nom == "": 
                    nom = input(f"Nom ({contacte['nom']}): ").title()
                    if nom == "":
                        nom = contacte["nom"]
                        break
                    if nom.isalpha():
                        break
                    else:
                        print("El nom només pot contindre caràcters alfanumèrics.")
                
                # Email
                while True:
                    email = input(f"Email ({contacte['email']}): ").lower()
                    if email == "":
                        email = contacte["email"]
                        break
                    if(re.search(formatEmail,email)):
                        break
                    else: 
                        print("El format del correu electrònic és invàlid.")
                
                # Telèfon
                telefons = []
                for usuari in agenda:
                    telefons.append(usuari["telefon"]) 

                while True:
                    try:
                        telefon = (input(f"Telèfon ({contacte['telefon']}): "))
                        if telefon == "":
                            telefon = contacte["telefon"]
                            break
                        telefon = int(telefon)
                        if len(str(telefon)) != 9:
                            print("El número de telèfon ha de tindre 9 dígits.")
                        elif telefon in telefons:
                            print("El número de telèfon ja està a l'agenda.")
                        else: 
                            telefon = str(telefon)
                            break
                    except ValueError:
                        print("Valor no numèric.")

                # Newsletter
                newsletter = ""
                if contacte['newsletter']:
                    mostrarNewsletter = "S"
                else: mostrarNewsletter = "N"
                while not newsletter in [True, False]:
                    newsletter = input(f"Newsletter ({mostrarNewsletter}): ").upper()
                    if telefon == "":
                        telefon = contacte["telefon"]
                        break
                    if newsletter == "S":
                        newsletter = True
                    elif newsletter == "N":
                        newsletter = False
                    
                contacte['nom'] = nom
                contacte['email'] = email
                contacte['telefon'] = telefon
                contacte['newsletter'] = newsletter

        if not trobat:
            print("Empleat no trobat.")
    input("\nPrèm Enter per a continuar")    

def esborrarContacte():
    if agenda == []:
        print("No hi han contactes afegits.")
    else:
        for contacte in agenda:
            print(f"{contacte['id']} - {contacte['nom']}")
        
        IDAEsborrar = int(input("Tria la ID de l'empleat que vols esborrar: "))
        trobat = False
        for contacte in agenda:
            if contacte["id"] == IDAEsborrar:
                agenda.remove(contacte)
                trobat = True
                print("Empleat esborrat.")
        if not trobat:
            print("Empleat no trobat.")

def importarAgenda():
    global agenda
    try:
        with open(path+file) as fitxerJson:
            agenda = json.load(fitxerJson)
            print("Agenda importada correctament.")
    except FileNotFoundError:
        print("El fitxer no existeix.")
    input("\nPrèm Enter per a continuar")
        
def exportarAgenda():

    if agenda == []:
        importar = ""
        while not importar in [True, False]:
            importar = input("No hi han contactes afegits, vols exportar l'agenda igualment? (S/N): ").upper()
            if importar == "S":
                importar = True
            elif importar == "N":
                importar = False
    if (agenda != []) or (importar == True):
        with open(path+file, 'w') as fitxerJson:
            json.dump(agenda, fitxerJson)
            print("Agenda exportada correctament.")
        input("\nPrèm Enter per a continuar")
    
while True:
    os.system("cls")
    print("─" * 25)
    print(" Pt3.4 - Agenda")
    print("─" * 25)
    print("[1] Afegir contacte")
    print("[2] Mostrar contactes")
    print("[3] Cercar contactes")
    print("[4] Modificar contactes")
    print("[5] Esborrar contactes")
    print("[6] Exportar a fitxer")
    print("[7] Importar de fitxer")
    print("[8] Sortir del programa")

    print("─" * 25)

    menu = input("Selecciona una opció: ")
    os.system("cls")

    if menu == "1":
        afegirContacte()
    elif menu == "2":
        mostrarAgenda()
    elif menu == "3":
        cercarContacte()
    elif menu == "4":
        modificarContacte()
    elif menu == "5":
        esborrarContacte()
    elif menu == "6":
        exportarAgenda()
    elif menu == "7":
        matriu = importarAgenda()
    elif menu == "8":
        print("Sortint del programa.")
        exit()