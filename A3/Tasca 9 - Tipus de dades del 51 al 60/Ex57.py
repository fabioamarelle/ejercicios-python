# Inicialitza el mòdul Datetime i la llista
from datetime import datetime
llistaDates = []

# Demana 20 dates, les afegeix a llistaDates
for i in range(20):
    dataStr = input("Introdueix una data en format 'YYYY-MM-DD': ")
    dataDatetime = datetime.strptime(dataStr,  "%Y-%m-%d")
    llistaDates.append(dataDatetime)

# Calcula i mostra les dates màxima i mínima
alumneVell = min(llistaDates)
alumneJove = max(llistaDates)

print(f"Data de l'alumne més jove: {alumneJove.date()}")
print(f"Data de l'alumne més vell: {alumneVell.date()}")

# Si l'any d'aquests dos alumnes 
if alumneVell.year == alumneJove.year:
    print("L'alumne més jove i el més vell han nascut al mateix any.")