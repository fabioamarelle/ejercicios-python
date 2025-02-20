from calculs import eleva
from calculs import calculadora


print("[1] Calculadora")
print("[2] Eleva")
funcio = int(input("Introdueix la funció: "))

if funcio == 1:
    num1 = input("Introdueix el primer nombre: ")
    num2 = input("Introdueix el segon nombre: ")
    operador = input("Introdueix l'operador: ")
    print(calculs.calculadora(num1, num2, operador))
if funcio == 2:
    base = input("Introdueix la base: ")
    exponent = input("Introdueix l'exponent: ")
    print(calculs.eleva(base,exponent))
