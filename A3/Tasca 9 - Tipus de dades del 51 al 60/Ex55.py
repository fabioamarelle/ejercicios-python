vector = []
for i in range(0,10):
    valor = input("Introdueix un valor: ")
    vector.append(valor)

vectorInvertit = []
for i in range(9,-1,-1):
    vectorInvertit.append(vector[i])

print("Vector:")
print(vector)

print("Vector invertit:")
print(vectorInvertit)