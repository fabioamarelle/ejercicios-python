any = int(input("Introdueix un any: "))
if any % 4 == 0 and any % 100 != 0 or any % 400 == 0:
    print(f"L'any {any} és un any de traspàs.")
else:
    print(f"L'any {any} no és un any de traspàs.")