n2e = int(input("Nº Monedes 2€: "))
n1e = int(input("Nº Monedes 1€: "))
n50c = int(input("Nº Monedes 0,50€: "))
n20c = int(input("Nº Monedes 0,20€: "))
n10c = int(input("Nº Monedes 0,10€: "))
total = (n2e * 2) + (n1e) + (n50c * 0.50) + (n20c * 0.20) + (n10c * 0.10)
totalaprox = round(total,2)         # Arrodoneix el total a dos decimals
print(f"El valor total de les teves monedes és de {totalaprox}€.")