pesRaim = int(input("Introdueix el nombre de quilos de raïm venuts: "))
preuInicial = int(input("Introdueix el preu inicial per quilo: "))
tipusRaim = input("Introdueix el tipus de raïm (A1, A2, B1, B2): ")

if tipusRaim == "A1":
    preuInicial = preuInicial + 0.20
elif tipusRaim == "A2":
    preuInicial = preuInicial + 0.30
elif tipusRaim == "B1":
    preuInicial = preuInicial - 0.30
elif tipusRaim == "B2":
    preuInicial = preuInicial - 0.50

resultat = pesRaim * preuInicial

print(f"El preu total és de {resultat}€.")