from datetime import datetime
import random, math, time

# He provat a calcular el temps d'execució amb dos mòduls diferents. El mòdul time és més precís quan calcula períodes de temps petits.

tempsAbansDatetime = datetime.now()
tempsAbansTime = time.perf_counter()

arrel1 = math.sqrt(random.randint(1,100))
arrel2 = math.sqrt(random.randint(1,100))
arrel3 = math.sqrt(random.randint(1,100))

tempsDespresDatetime = datetime.now()
tempsDespresTime = time.perf_counter()

diferenciaDatetime = abs(tempsDespresDatetime-tempsAbansDatetime)
diferenciaTime = abs(tempsDespresTime-tempsAbansTime)

print(f"Resultat de les arrels: {arrel1}, {arrel2}, {arrel3}")
print(f"El programa ha tardat {diferenciaDatetime.microseconds} microsegons en calcular les arrels. (Càlcul amb Datetime)") # A vegades pot donar uns 1000 microsegons, però normalment dóna 0. No és precís.
print(f"El programa ha tardat {round(diferenciaTime*1000000,2)} microsegons en calcular les arrels. (Càlcul amb Time)")
