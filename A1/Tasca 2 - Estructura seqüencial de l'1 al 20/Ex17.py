dataSortida = input("Introdueix la hora de sortida (Format HH:MM:SS): ")
horaSortida, minutSortida, segonSortida = dataSortida.split(":")            # Separa hores, minuts i segons utilitzant el símbol ":"
horaSortida = int(horaSortida) * 3600                                       # 1 hora són 3600 segons
minutSortida = int(minutSortida) * 60                                       # 1 minut són 60 segons

segons = int(segonSortida) + horaSortida + minutSortida                     # Suma hores, minuts i segons en format segons
tempsArribada = int(input("Introdueix la distància en segons: "))
segons = int(tempsArribada) + int(segons)                                   # Suma la hora actual i els segons fins a l'arribada
horesA = segons // 3600                                                     
minutsA = (segons // 60) - (horesA * 60)
segonsA = segons % 60


print(f"La hora d'arribada serà {horesA}:{minutsA}:{segonsA}")              # Pot superar les 24 hores, es podria arreglar amb "if horesA > 24: horesA = horesA % 24"
