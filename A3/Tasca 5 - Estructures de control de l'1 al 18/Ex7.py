a = int(input("Introdueix la base: "))
b = int(input("Introdueix l'exponent: "))

if b > 0:
    # L'exponent és positiu
    c = a ** b
    print(f"{a}^{b} = {c}")
elif b < 0:
    # L'exponent és negatiu
    c = 1 / a ** abs(b)
    print(f"{a}^{b} = {c}")
elif b == 0:
    # L'exponent és zero
    c = 1
    print(f"{a}^{b} = {c}")