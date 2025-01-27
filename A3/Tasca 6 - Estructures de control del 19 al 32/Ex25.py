suma = []
for i in range(10):
    num = int(input("Introdueix un nombre: "))
    suma.append(num)

mitjanaAritmetica = sum(suma) / len(suma)

print(f"La mitjana aritmètica dels nombres és {mitjanaAritmetica}")