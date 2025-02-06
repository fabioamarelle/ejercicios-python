import os
treballadors = [
    {
        "nom": "Marc ",
        "edat": 28,
        "salari": 1500
    },
    {
        "nom": "Anna ",
        "edat": 22,
        "salari": 1400
    },
    {
        "nom": "Maria",
        "edat": 40,
        "salari": 2000
    },
    {
        "nom": "Jaume",
        "edat": 41,
        "salari": 1800
    },
    {
        "nom": "Manel",
        "edat": 18,
        "salari": 1200
    },
    {
        "nom": "Rosa ",
        "edat": 49,
        "salari": 1800
    },
]


def llistarTreballadors():
    os.system("cls")
    print("Nom\t| Edat\t| Salari")
    for treballador in treballadors:
        print("─" * 35)
        print(f"{treballador["nom"]}\t| {treballador["edat"]}\t| {treballador["salari"]}")
    input()

def llistarNoms():
    os.system("cls")
    for treballador in treballadors:
        print(treballador["nom"])
    input()


def afegirTreballadors():
    os.system("cls")
    print("Afegint un nou treballador:")
    # Afegeix treballadors, valida que edat i salari siguin numèrics.
    nom = input("Introdueix el nom: ")

    while True:
        try:
            edat = int(input("Introdueix l'edat: "))
            break
        except ValueError:
            print("L'edat ha de ser un valor numèric.")
            
    while True:
        try:
            salari = int(input("Introdueix el salari: "))
            break
        except ValueError:
            print("El salari ha de ser un valor numèric.")

    treballadors.append(
        {
        "nom": nom,
        "edat": edat,
        "salari": salari
        }
    )
    print("Treballador afegit.")
    input()

def llistarSalariMesAlt():
    os.system("cls")
    salaris = []
    for treballador in treballadors:
        salaris.append(treballador["salari"])

    print("Nom\t| Edat\t| Salari")
    for treballador in treballadors:
        if treballador["salari"] == max(salaris):
            print("─" * 35)
            print(f"{treballador["nom"]}\t| {treballador["edat"]}\t| {treballador["salari"]}")

    print("\n")
    print(f"El salari màxim és de {max(salaris)}€.")
    
    input()

def treballadorsMenorsDe35():
    os.system("cls")
    treballadorsMenors = []
    for treballador in treballadors:
        if treballador["edat"] < 35:
            treballadorsMenors.append(treballador["edat"])

    print("Nom\t| Edat\t| Salari")
    for treballador in treballadors:
        if treballador["edat"] < 35:
            print("─" * 35)
            print(f"{treballador["nom"]}\t| {treballador["edat"]}\t| {treballador["salari"]}")

    print("\n")
    print(f"Hi ha {len(treballadorsMenors)} treballadors menors de 35 anys.")
    input()

def diccionarisAMatriu():
    os.system("cls")
    matriuTreballadors =[]
    for treballador in treballadors:
        matriuTreballadors.append([treballador["nom"], treballador["edat"], treballador["salari"]])
    for treballador in matriuTreballadors:
        print(*treballador)
    input()
def main():
    while True:
        os.system("cls")
        print("Base de dades dels treballadors")
        print("-----------------------------------")
        print("[1] Llistar treballadors")
        print("[2] Llistar noms dels treballadors")
        print("[3] Afegir treballadors")
        print("[4] Llistar els salaris més alts")
        print("[5] Comptar treballadors menors de 35 anys")
        print("[6] Transformar diccionaris a matriu")
        print("-----------------------------------")

        menu = input("Tria una opció:")
        if menu == "1":
            llistarTreballadors()
        elif menu == "2":
            llistarNoms()        
        elif menu == "3":
            afegirTreballadors()
        elif menu == "4":
            llistarSalariMesAlt()
        elif menu == "5":
            treballadorsMenorsDe35()
        elif menu == "6":
            diccionarisAMatriu()
        else:
            print("Error.")

main()