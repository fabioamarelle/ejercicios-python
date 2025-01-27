class Persona:
    def __init__ (self, nom, edat):
        self.nom = nom
        self.edat = edat

# Afegir __str__ permet canviar el que es mostra en imprimir l'objecte.
    def __str__ (self):
        return f"Nom: {self.nom}, Edat: {self.edat}"

persona1 = Persona("Manel", 19)
print(persona1) # Ara es mostra el que s'ha afegit a __str__