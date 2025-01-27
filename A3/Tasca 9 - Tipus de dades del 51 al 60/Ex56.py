# Demana deu nombres i els afegeix a la llista 
vector = []
for i in range(0,10):
    valor = input("Introdueix un valor: ")
    vector.append(valor)

# Mostra la llista a l'usuari
print(vector)

cerca = 1           # Inicialitza la variable

# Bucle fins que l'usuari introdueixi zero. Així permet fer més d'una cerca per execució.
while cerca != 0:
    cerca = int(input("Introdueix una posició a buscar. Introdueix 0 per sortir del programa: "))
    if cerca == 0:
        print("Sortint del programa.")

    elif cerca not in range(0,len(vector)+1):
        print(f"No hi ha cap valor a la posició {cerca}.")
        
    else:
        print(f"El valor a la posició {cerca} és {vector[cerca-1]}.")