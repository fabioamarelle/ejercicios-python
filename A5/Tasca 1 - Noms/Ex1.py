import os

filename = "/fitxers/noms.txt"
path = os.getcwd()


# Funció que valida el text sigui alfanumèric, i canvia la primera lletra a majúscula
def validar(text, tipus):
    while not text.isalpha():
        print("Text invàlid")
        text = input(f"Torna a introduir el {tipus}: ")
    return text.title()

def afegirUsuari():
    nom = input("Introdueix un nom: ")
    nom = validar(nom, "nom")

    cognom = input("Introdueix un cognom: ")
    cognom = validar(cognom, "cognom")

    with open((path+filename), "a") as txt:     # L'argument "a" fa que no s'esborri el text del fitxer
        txt.write(f"{nom} {cognom} \n")

# Aquest codi no s'executarà en importar els mòduls
if __name__ == "__main__":      
    for i in range(5):
        print(f"Persona Nº{i+1}")
        afegirUsuari()
        os.system("cls")


