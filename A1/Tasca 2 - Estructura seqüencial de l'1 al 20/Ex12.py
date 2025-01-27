x1 = int(input("Introdueix el valor x del primer punt: "))
y1 = int(input("Introdueix el valor y del primer punt: "))
x2 = int(input("Introdueix el valor x del segon punt: "))
y2 = int(input("Introdueix el valor y del segon punt: "))

# De la mateixa forma que a l'exercici 11, calcula la diferència dels nombres
x = abs(x1 - x2)
y = abs(y1 - y2)

dist = ((x**2) + (y**2))**0.5
print(f"La distància és {dist}.")