# El codi també ha de revisar que la frase no sigui un conjunt d'espais, si no donarà errors
continuar = True

while continuar:
    frase = input("Introdueix una frase: ")
    if frase == "":
        print("La frase és buida.")
    else: 
        # Revisa cada lletra individualment, si troba qualsevol caràcter que no sigui un espai para el bucle
        for lletra in frase: 
            if lletra != " ":
                continuar = False
                
nParaules = len(frase.split(" "))
print(f"Nombre de paraules: {nParaules}")