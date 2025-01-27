# Qualificacions parcials (55%)
parcial1 = float(input("Introdueix la primera qualificació parcial: "))
parcial2 = float(input("Introdueix la segona qualificació parcial: "))
parcial3 = float(input("Introdueix la tercera qualificació parcial: "))
mitjanaparcial = (parcial1 + parcial2 + parcial3) / 3

# Examen final (30%)
examenf = float(input("Introdueix la nota de l'examen final: "))

# Treball final (15%)
treballf = float(input("Introdueix la nota del treball final: "))

notafinal = (mitjanaparcial * 0.55 + examenf * 0.30 + treballf * 0.15)
print(notafinal)