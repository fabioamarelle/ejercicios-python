import math

x1 = int(input("Introdueix el punt central x1: "))
x2 = int(input("Introdueix el punt central x2: "))
y1 = int(input("Introdueix el punt central y1: "))
y2 = int(input("Introdueix el punt central y2: "))
r1 = int(input("Introdueix el radi de la primera circumferència: "))
r2 = int(input("Introdueix el radi de la segona circumferència: "))


distancia = math.sqrt(((x2-x1)**2 + (y2-y1)**2))

if distancia == 0:
    print("Són circumferències concèntriques.")
elif distancia > (r1+r2):
    print("Són circumferències exteriors.")
elif distancia > 0 and distancia < abs(r1-r2):
    print("Són circumferències interiors.")
elif distancia == (r1+r2):
    print("Són circumferències tangents exteriors.")
elif distancia > abs(r1-r2):
    print("Són circumferències tangents interiors.")
elif distancia < (r1+r2) and distancia > abs(r1-r2):
    print("Són circumferències assecants.")
else:
    print("Error")