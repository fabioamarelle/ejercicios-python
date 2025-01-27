nomUsuari = input("Introdueix el teu nom: ")

class Persona:
    def __init__ (self, nom, edat):
        self.nom = nom
        self.edat = edat

    def __str__ (self):
        return f"Nom: {self.nom}, Edat: {self.edat}"
    
    def presenta(self):
        print(f"Hola, em dic {self.nom} i tinc {self.edat} anys.")

    def saluda(self):
        print(f"Hola {nomUsuari}, sóc en {self.nom}.")

persona1 = Persona("Manel", 19)

persona1.saluda()