nombre = 1
suma = 0

nombre = input("Introdueix nombres enters separats per comes: ")
llistaNombres = nombre.split(",")

# No es pot calcular la suma (per a la mitjana) amb sum()
for num in llistaNombres:
    suma += int(num)



print(f"Mínim: {min(llistaNombres)}")
print(f"Posició: {llistaNombres.index(min(llistaNombres))+1}")
print()
print(f"Màxim: {max(llistaNombres)}")
print(f"Posició: {llistaNombres.index(max(llistaNombres))+1}")
print()
print(f"Mitjana: {suma/len(llistaNombres)}")