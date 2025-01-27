a = int(input("Introdueix el primer nombre: "))
b = int(input("Introdueix el segon nombre: "))

if b == 0:
    print(f"No es pot dividir per zero.")
else:
    c = a / b
    print(f"{a} / {b} = {c}")