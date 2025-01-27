llistaNombres = []
numero = 1

while numero != 0:
    numero = int(input("Introdueix un nombre: "))
    if numero != 0:             # Fa que no s'introdueixi el zero al final 
        llistaNombres.append(numero)

print(f"La llista és {llistaNombres}")
print(f"Suma dels nombres: {sum(llistaNombres)}")
print(f"Nombres introduïts: {len(llistaNombres)}")
