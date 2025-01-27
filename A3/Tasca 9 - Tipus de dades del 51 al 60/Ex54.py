vector = []
for i in range(0,10):
    valor = input("Introdueix un valor: ")
    vector.append(valor)

vector.insert(0, vector[-1])     # Agafa l'últim valor i el còpia al començament de la llista
vector.pop(-1)                  # Elimina l'últim valor

print(vector)