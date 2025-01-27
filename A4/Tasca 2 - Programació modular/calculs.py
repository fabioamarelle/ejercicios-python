
def calculadora(num1, num2, operador):
    operadorsPossibles = ["+","-","*","/"]

    # Validacions del primer número
    while True:
        try:
            num1 = int(num1)
            break
        except ValueError:
            print("El format del primer nombre no és correcte.")
            num1 = input("Introdueix el primer nombre: ")

    # Validacions del segon número
    while True:
        try:
            num2 = int(num2)
            break
        except ValueError:
            print("El format del segon nombre no és correcte.")
            num2 = input("Introdueix el segon nombre: ")

    if not operador in operadorsPossibles:
        print("Operador incorrecte.")
        while True:
            operador = input("Introdueix l'operador: ")
            if operador in operadorsPossibles:
                break
            else:
                print("Operador incorrecte.")

    if operador == "+":
        return (f"Resultat: {num1} {operador} {num2} = {num1 + num2}")

    elif operador == "-":
        return (f"Resultat: {num1} {operador} {num2} = {num1 - num2}")
    
    elif operador == "*":
        return (f"Resultat: {num1} {operador} {num2} = {num1 * num2}")
    
    elif operador == "/":
        if num2 == 0:
            print("No es pot dividir per zero.")
            exit()
        else:
            return (f"Resultat: {num1} {operador} {num2} = {num1 / num2}")
    else: 
        print("Operador incorrecte. ")

def eleva(base,exponent):
    while True:
        try:
            base = int(base)
            break
        except ValueError:
            base = input("Introdueix la base: ")
    while True:
        try:
            exponent = int(exponent)
            break
        except ValueError:
            exponent = input("Introdueix l'exponent: ")
    return (f"Resultat: {base} ^ {exponent} = {base**exponent}")



