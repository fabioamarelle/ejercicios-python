nota = int(input("Introdueix la nota: "))
edat = int(input("Introdueix l'edat: "))
sexe = str(input("Introdueix el gènere (M, F): "))
if not sexe == "M" and not sexe == "F":
    print("El gènere ha de ser M o F.")
elif nota >= 5 and edat >= 18 and sexe == "F":
    print("ACCEPTADA")
elif nota >= 5 and edat >= 18 and sexe == "M":
    print("POSSIBLE")
else:
    print("NO ACCEPTADA")