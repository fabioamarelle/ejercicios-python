cadena = input("Introdueix una cadena de text: ")
nParaules = 1               # Comença sent 1. La primera paraula no té un espai abans.

for lletra in cadena:
    if lletra == " ":       # Per cada espai que troba:
        nParaules += 1      # Afegeix 1 al comptador nParaules. 

# També es podria fer així sense estructures de control:
# nParaules = len(cadena.split(" "))

print(f"{cadena} té {nParaules} paraules")