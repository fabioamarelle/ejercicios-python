import math

class Cercle: 
    def __init__ (self, radi):
        self.radi = radi

    def areaCercle(self):
        self.area = round((math.pi * self.radi ** 2),2)     # àrea = π*r^2
        print(f"L'àrea d'un cercle amb radi {self.radi} és {self.area}.")
    
# Aquest objecte només té un atribut, el radi, i es demana a l'usuari.
cercle1 = Cercle(int(input("Introdueix el radi del cercle: ")))

cercle1.areaCercle()