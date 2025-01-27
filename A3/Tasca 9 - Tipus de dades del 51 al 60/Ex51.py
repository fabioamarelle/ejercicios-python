vector = []
while len(vector) != 10:
    valor = int(input("Introdueix un número: "))
    vector.append(valor)
print(vector)
print(f"La suma és {sum(vector)}.")