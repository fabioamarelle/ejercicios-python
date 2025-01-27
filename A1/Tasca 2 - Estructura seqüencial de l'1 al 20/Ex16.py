velocitat1 = int(input("Introdueix la velocitat del primer vehicle en kilòmetres per hora: "))
velocitat2 = int(input("Introdueix la velocitat del segon vehicle en kilòmetres per hora: "))
distancia = int(input("Introdueix la distància entre els vehicles en kilòmetres: "))

diferencia = abs(velocitat1 - velocitat2)   # De la mateixa forma que a l'exercici 11, calcula la diferència dels nombres
resultat = (distancia / diferencia) * 60           # El resultat és igual a la distància dividida entre la diferència de velocitats.
print(f"El vehicle més ràpid tardarà {resultat} minuts en adelantar al vehicle més lent")