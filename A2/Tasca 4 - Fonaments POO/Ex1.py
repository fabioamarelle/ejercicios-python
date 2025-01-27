# Crea una classe amb els atributs nom i edat
class Persona:
    def __init__ (self, nom, edat):
        self.nom = nom
        self.edat = edat

# Crea un objecte amb els seus atributs
persona1 = Persona("Manel", 19)

print(persona1) # Mostra l'adreça a la memòria de l'objecte