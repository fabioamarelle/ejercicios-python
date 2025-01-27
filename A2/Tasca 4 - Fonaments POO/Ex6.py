class Producte:
    def __init__ (self, nom, preu, descompte):
        self.nom = nom
        self.preu = preu
        self.descompte = descompte

    def preuAmbDescompte(self):
        self.preuDescompte = round(self.preu - (self.preu * (self.descompte / 100)),2)
        print(f"El preu amb descompte del producte {self.nom} és {self.preuDescompte}€")


# Crea un objecte ón tots els atributs els introdueix l'usuari.
producte1 = Producte(
    input("Introdueix el nom del producte: "),
    float(input("Introdueix el preu del producte: ")),
    float(input("Introdueix el descompte: "))
)
# Es crida el mètode que calcula el preu amb descompte i el mostra per pantalla
producte1.preuAmbDescompte()