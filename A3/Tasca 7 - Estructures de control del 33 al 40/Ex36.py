frase = input("Introdueix una frase: ")
vocals = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]     # Llista amb totes les vocals

for lletra in frase:
    if lletra in vocals:                                        # Si la lletra està a la llista de les vocals:
        print(f"La primera vocal és '{lletra.upper()}'")
        break