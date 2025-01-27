catet1 = float(input("Introdueix el primer catet: "))
catet2 = float(input("Introdueix el segon catet: "))
# La fòrmula per calcular la hipotenusa és a^2 + b^2 = c^2, sent a i b els catets i c la hipotenusa
# S'ha de fer l'arrel quadrada i, per no haver d'importar mòduls, es pot elevar a 0.5, que dóna el mateix resultat.
hipotenusa = ((catet1**2) + (catet2**2))**0.5       
print(f"La hipotenusa és {hipotenusa}.")

