class Calculadora:
# Crea quatre mètodes estàtics per sumar, restar, multiplicar i dividir
    @staticmethod
    def sumar(a, b):
        return a + b
    @staticmethod
    def restar(a, b):
        return a - b
    @staticmethod
    def multiplicar(a, b):
        return a * b
    @staticmethod
    def dividir(a, b):
        return a / b

a = int(input("Introdueix el primer número: "))
b = int(input("Introdueix el segon número: "))

# Crida als quatre mètodes estàtics
suma = Calculadora.sumar(a, b)
resta = Calculadora.restar(a, b)
multiplicacio = Calculadora.multiplicar(a, b)
divisio = round(Calculadora.dividir(a, b),2)

# Mostra els quatre resultats
print(f"{a} + {b} = {suma}")
print(f"{a} - {b} = {resta}")
print(f"{a} * {b} = {multiplicacio}")
print(f"{a} / {b} = {divisio}")