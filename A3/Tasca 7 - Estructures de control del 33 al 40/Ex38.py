clau = "eureka"
intents = 3

while intents > 0:
    intentClau = input("Introdueix la clau: ")
    if intentClau == clau:
        print("Contrasenya correcta")
        exit()
    else:
        print("Contasenya incorrecta")
        intents = intents - 1
print("Has esgotat tots els intents possibles.")