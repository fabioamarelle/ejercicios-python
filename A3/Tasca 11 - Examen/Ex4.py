nIntents = 4
contrasenya = "benvingut"

while nIntents != 0:
    intent = input("Introdueix la contrasenya: ")
    # Si l'intent és correcte, acaba el programa
    if intent == contrasenya:
        print("Contrasenya correcta.")
        exit()
    # Si l'intent és incorrecte, resta un intent
    else:
        print("Contrasenya incorrecta.")
        nIntents -= 1
        print(f"Queden {nIntents} intents.")
    
print("Has esgotat els intents. El sistema s'ha bloquejat per seguretat.")