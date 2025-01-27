llista = []
num = 1
nombreNegatiu = False

while num != 0:
    num = int(input("Introdeix un nombre enter. Introdueix 0 per finalitzar el programa: "))
    llista.append(num)
    if num < 0:
        nombreNegatiu = True 

print(llista)
if nombreNegatiu == True:
    print("Hi ha algun nombre negatiu a la seqüència.")
else:
    print("Tots els nombres a la seqüència són positius.")
