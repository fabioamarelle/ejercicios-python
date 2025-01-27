import random
class dau:
    @staticmethod
    def tirarDau():
        return random.randint(1,6)    

resultats = dau.tirarDau(), dau.tirarDau(), dau.tirarDau(), dau.tirarDau()  # Crea una llista amb quatre nombres aleatoris

print(*resultats) # Afegir * al print elimina les comes i mostra els nombres separats per un espai
