soubase = float(input("Introdueix el sou base: "))
venda1 = float(input("Introdueix el valor de la primera venda: "))
venda2 = float(input("Introdueix el valor de la segona venda: "))
venda3 = float(input("Introdueix el valor de la tercera venda: "))
total = soubase + ((venda1 + venda2 + venda3) * 0.10)       # Suma el sou base i el 10% de totes les vendes
print(f"El sou total és {total}.")