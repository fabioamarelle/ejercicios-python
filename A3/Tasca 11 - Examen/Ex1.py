# Inicialitza les variables
iteracions = 0
preuProducte = 0
llistaProductes = []
llistaProductesLimit = []

# Crea una llista amb els preus, també valida el format
while preuProducte != "":
    iteracions += 1
    preuProducte = input(f"Introdueix el preu del producte Nº{iteracions}: ")
    # Si el producte és un número (també permet decimals), l'afegeix a la llista
    try:
        preuProducte = float(preuProducte)
        llistaProductes.append(preuProducte)
    # Si no, dóna error i no l'afegeix a la llista
    except ValueError:
        if preuProducte != "":
            print("Introdueix un nombre.")

# Demana el preu límit, també valida el format
while True:
    preuLimit = input("Introdueix el preu límit: ")
    try: 
        preuLimit = float(preuLimit)
        break
    except ValueError:
        print("Introdueix un nombre.")

# Si el preu és superior (no compta iguals) al límit, l'afegeix a una llista 
for preu in llistaProductes:
    if preu > preuLimit:
        llistaProductesLimit.append(preu)

# Calcula el percentatge, arrodoneix 2 decimals
percentatgeLimit = round((len(llistaProductesLimit)/len(llistaProductes)*100),2)

# Mostra els resultats
print(f"Preus dels productes: {llistaProductes}")
print(f"Preus dels productes que superen el límit: {llistaProductesLimit}")
print(f"Percentatge de productes que superen el límit: {percentatgeLimit}%")