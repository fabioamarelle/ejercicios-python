assignatures = ["Anglès professional", "Llenguatges de marques", "Bases de dades", "Programació", "Entorns de desenvolupament", "Digitalització", "Sostenibilitat"]
llistaNotes = []

for i in range(0,7):
    nota = int(input(f"Introdueix la nota del mòdul {assignatures[i]}: "))
    llistaNotes.append(nota) 

print("Butlletí de notes")
for i in range(0,7):
    print(f"{assignatures[i]}: {llistaNotes[i]}")