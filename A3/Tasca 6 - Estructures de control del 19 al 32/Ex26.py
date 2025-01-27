partPractica = 1
partProblemes = 1
partTeorica = 1

while partPractica != 0 and partProblemes != 0 and partTeorica != 0:
    partPractica = float(input("Introdueix la nota de la part pràctica: "))
    partProblemes = float(input("Introdueix la nota dels problemes: "))
    partTeorica = float(input("Introdueix la nota de la teoria: "))
    if partPractica > 10 or partPractica < 1 or partProblemes > 10 or partProblemes < 1 or partTeorica > 10 or partTeorica < 1:
        print("Les notes han de ser un nombre entre 1 i 10.")      
    else:
        notafinal = round((partPractica * 0.1 + partProblemes * 0.5 + partTeorica * 0.4),2)
        print(f"La nota final és {notafinal}")

print("Sortint del programa.")