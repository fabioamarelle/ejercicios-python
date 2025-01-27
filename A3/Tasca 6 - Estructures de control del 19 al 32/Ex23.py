horesSetmanals = int(input("Introdueix les hores setmanals treballades: "))
preuHora = int(input("Introdueix el preu per hora treballada: "))
if horesSetmanals > 40:
    paga = (((horesSetmanals - 40) * preuHora) * 1.5) + 40 * preuHora
else:
    paga = horesSetmanals * preuHora

print(f"El treballador cobrarà {paga}€")