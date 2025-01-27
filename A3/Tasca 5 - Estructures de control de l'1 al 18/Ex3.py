a = int(input("Introdueix un nombre: "))
if a % 2 == 0:
    print(f"{a} és un nombre parell.")
elif not a % 2 == 0:
    print(f"{a} és un nombre imparell.")
else:
    print("Error.")