inicials = ""

nomComplet = input("Introdueix el teu nom i cognoms: ")
nomCompletLlista = nomComplet.split()                       # Crea una llista amb un ítem per cada nom i cognom

for paraula in nomCompletLlista:                            # Per cada ítem a la llista (paraules):
    inicials += paraula[0].upper()                          # Agafa la primera lletra (posició 0), la posa en majúscules i l'afegeix a la variable inicials

print(f"Les inicials són {inicials}")

