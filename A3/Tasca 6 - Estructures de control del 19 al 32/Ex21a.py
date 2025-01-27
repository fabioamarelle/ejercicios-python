nImparells = 0
sumaImparells = 0
llista = []

while nImparells < 10:
    num = int(input("Introdeix un nombre enter: "))
    if num % 2 == 0:
        llista.append(num)
    else:
        llista.append(num)
        sumaImparells += num
        nImparells += 1

print(f"{llista} -> {sumaImparells}")