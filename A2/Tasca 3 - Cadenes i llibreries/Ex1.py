from datetime import datetime       # Importa el mòdul DateTime

data1Str = input("Introdueix una data en format 'YYYY-MM-DD': ")
data2Str = input("Introdueix una altre data en format 'YYYY-MM-DD': ")

data1Datetime = datetime.strptime(data1Str,  "%Y-%m-%d")        # Converteix l'input de l'usuari (str) al format datetime.
data2Datetime = datetime.strptime(data2Str,  "%Y-%m-%d")

diferencia = abs(data1Datetime - data2Datetime)

print(f"La diferència és de {diferencia.days} dies") # .days només mostra els dies, si no també mostraria les hores de diferència

