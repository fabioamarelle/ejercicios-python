cadena = input("Introdueix una cadena de text: ")
comptador = len(cadena) - 1             # El comptador és el número de caràctes - 1 (per tindre en compte la posició 0 de for)

for lletra in cadena:
    print(cadena[comptador], end="")    # Primer agafa la última lletra, després la penúltima, etc.
    comptador -= 1

# També es podria fer sense bucles, amb reversed(cadena)