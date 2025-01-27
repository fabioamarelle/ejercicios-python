# Inicialitza les variables
alumnes = 0
alumnesAprovats = 0
alumnesSuspesos = 0
nota = 0
llistaNotes = []

# Demana notes i verifica el format
while nota != "":
    nota = input("Introdueix la nota d'un alumne: ")

    # .isdigit() no funciona amb variables float i, com les notes poden ser valors amb decimals, he hagut d'utilitzar except ValueError per comprovar si és un float 

    if nota != "":                                              # Si no és un espai en blanc:
        try:                                          
            notaFloat = float(nota)                             # Intenta convertir a float
        except ValueError:                                      # Si dóna error:
            print("Introdueix un número entre 0 i 10.")
    
    if nota != "":                                              # Si no és un espai en blanc:
        if not 0 <= notaFloat <= 10:                            # Revisa que està entre 0 i 10
            print("Introdueix un número entre 0 i 10.")
        else:                     
            llistaNotes.append(notaFloat)                       # Afegeix al vector amb les notes


# Calcula els alumnes totals, aprovats i suspesos
for i in llistaNotes:
    if i >= 5:
        alumnesAprovats += 1
        alumnes += 1
    else:
        alumnesSuspesos += 1
        alumnes += 1

# Mostra els resultats
print()
print("Llista de notes:", *llistaNotes)
print(f"Alumnes aprovats: {alumnesAprovats}")
print(f"Alumnes suspesos: {alumnesSuspesos}")
print(f"Percentatge d'alumnes aprovats: {round((alumnesAprovats / alumnes * 100),2)}%")
    
