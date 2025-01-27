class Persona:
    def __init__ (self, nom, edat):
        self.nom = nom
        self.edat = edat

    def __str__ (self):
        return f"Nom: {self.nom}, Edat: {self.edat}"
    
# Crea el mètode "presenta".
    def presenta(self):
        print(f"Hola, em dic {self.nom} i tinc {self.edat} anys.")

persona1 = Persona("Manel", 19)

persona1.presenta()