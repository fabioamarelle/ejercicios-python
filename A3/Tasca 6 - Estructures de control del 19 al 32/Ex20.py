num = 1
while num != 0:
    num = int(input("Introdeix un nombre enter. Introdueix 0 per finalitzar el programa: "))
    if num % 2 == 0:
        print(f"{num}, parell")
    else:
        print(f"{num}, imparell")
        