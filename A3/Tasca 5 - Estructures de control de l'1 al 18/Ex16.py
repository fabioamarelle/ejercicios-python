tempsTrucada = int(input("Introdueix el nombre de minuts que dura la trucada: "))
diaTrucada = int(input("Introdueix el dia de la setmana en número (1-7): "))
tornTrucada = input("Introdueix el torn (Matí/Tarda): ")

# Verificacions a variables
if tempsTrucada < 0:
    print("La trucada no pot ser un nombre negatiu.")
elif diaTrucada < 1 or diaTrucada > 7:
    print("Introdueix un nombre entre 1 i 7.")
elif not tornTrucada == "Matí" and not tornTrucada == "Tarda":
    print("El torn ha de ser Matí o Tarda")

# Càlculs amb el temps de la trucada
elif tempsTrucada <= 5:
    # Els primers 5 minuts costen 1 euro
    preu = tempsTrucada * 1 
elif tempsTrucada <= 8:
    preu = (tempsTrucada * 1) + ((tempsTrucada - 5) * 0.80)
elif tempsTrucada <= 10:
    preu = (tempsTrucada * 1) + ((tempsTrucada - 5) * 0.80) + ((tempsTrucada - 8) * 0.70)
elif tempsTrucada > 10:
    preu = (tempsTrucada * 1) + ((tempsTrucada - 5) * 0.80) + ((tempsTrucada - 8) * 0.70) + ((tempsTrucada - 10) * 0.50)
print(f"Cost de la trucada: {preu}€")

if diaTrucada == 7:
    # Es carrega un impost de 3%
    preu = preu + (preu * 0.03)
elif tornTrucada == "Matí":
    # Es carrega un impost de 15%
    preu = preu + (preu * 0.15)
elif tornTrucada == "Tarda":
    # Es carrega un impost de 10%
    preu = preu + (preu * 0.10)
else:
    print("Error")
print(f"Cost de la trucada després d'impostos: {preu}€")