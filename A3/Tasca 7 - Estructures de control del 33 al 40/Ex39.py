nombre = 1
llistaNombres = []

while nombre != 0:
    nombre = int(input("Digam nombres enters: "))       # Demana un nombre
    if nombre != 0: llistaNombres.append(nombre)        # Afegeix el nombre a la llista (si no és 0)



print(f"Mínim: {min(llistaNombres)}")                       # Mínim
print(f"Màxim: {max(llistaNombres)}")                       # Màxim
print(f"Mitjana: {sum(llistaNombres)/len(llistaNombres)}")  # Mitjana (suma / quantitat de nombres)