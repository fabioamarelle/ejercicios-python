import random
from datetime import datetime

# Genera tres nombres al atzar, la hora, minuts, i segons
h = random.randint(0,23)
m = random.randint(0,59)
s = random.randint(0,59)

# Dóna el format Datetime als nombres generats automàticament d'una forma semblant a l'Exercici 1
horaAleatoria = f"{h}:{m}:{s}"
horaAleatoriaDatetime = datetime.strptime(horaAleatoria, "%H:%M:%S")

# Per a que estigui al mateix format que horaAleatoria i no agafi els dies, converteix només la hora actual a string i després a Datetime. 
horaActual = datetime.now().time().strftime('%H:%M:%S')
horaActualDatetime = datetime.strptime(horaActual, "%H:%M:%S")

# Amb les dues variables en el mateix format, es pot calcular la diferència
diferencia = abs(horaAleatoriaDatetime - horaActualDatetime)

print(f"Hora aleatoria: {horaAleatoria}")
print(f"Hora actual: {horaActual}")
print(f"Diferència: {diferencia}")