# Defineix funcions
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b

# Defineix les variables
a = int(input("Introdueix el primer número: "))
b = int(input("Introdueix el segon número: "))

# Crida les funcions
suma = sumar(a, b)
resta = restar(a, b)
multiplicacio = multiplicar(a, b)
divisio = round(dividir(a, b),2)

# Mostra els resultats
print(f"{a} + {b} = {suma}")
print(f"{a} - {b} = {resta}")
print(f"{a} * {b} = {multiplicacio}")
print(f"{a} / {b} = {divisio}")