base = int(input("Introdueix la base del rectangle: "))
altura = int(input("Introdueix l'altura del rectangle: "))
perimetre = (base + altura) * 2         # El perímetre és la suma de tots els costats. 
area = base * altura                    # L'àrea d'un rectangle és la base multiplicada per l'altura
print(f"El perímetre és: {perimetre}")
print(f"L'àrea és: {area}")