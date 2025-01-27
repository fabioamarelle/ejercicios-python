a = int(input("Introdueix el primer nombre: "))
b = int(input("Introdueix el segon nombre: "))
c = int(input("Introdueix el tercer nombre: "))

if a**2 + b**2 == c**2:
    print("És un triangle rectangle.")
elif a == b or a == c or b == c:
    print("És un triangle isòsceles")
elif a == b and a == c:
    print("És un triangle equilàter")
else:
    print("És un triangle escalè.")