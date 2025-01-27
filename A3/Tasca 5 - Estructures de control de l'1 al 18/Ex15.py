nAlumnes = int(input("Introdueix el nombre d'alumnes: "))
if nAlumnes <= 0: 
    print("El nombre d'alumnes no pot ser negatiu o zero.")
elif nAlumnes >= 100:
    print("Hi ha 100 alumnes o més. Per cada alumne s'han de pagar 65€.")
    preuAutobus = nAlumnes * 65
    print(f"Renda de l'autobús: {preuAutobus}€")
elif nAlumnes >= 50:
    print("Hi ha entre 50 i 99 alumnes. Per cada alumne s'han de pagar 70€.")
    preuAutobus = nAlumnes * 70
    print(f"Renda de l'autobús: {preuAutobus}€")
elif nAlumnes >= 30:
    print("Hi ha entre 30 i 49 alumnes. Per cada alumne s'han de pagar 95€.")
    preuAutobus = nAlumnes * 95
    print(f"Renda de l'autobús: {preuAutobus}€")
elif nAlumnes > 30:
    print("Hi ha menys de 30 alumnes. La renda de l'autobús és de 4000€.")
    preuAutobus = 4000
    print(f"Renda de l'autobús: {preuAutobus}€")