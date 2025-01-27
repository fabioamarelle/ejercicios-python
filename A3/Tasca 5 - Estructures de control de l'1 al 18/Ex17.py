resultatDau = int(input("Introdueix el resultat de tirar un dau de sis cares: "))

if resultatDau == 1:
    print("La cara oposada és el sis")
elif resultatDau == 2:
    print("La cara oposada és el cinc")
elif resultatDau == 3:
    print("La cara oposada és el quatre")
elif resultatDau == 4:
    print("La cara oposada és el tres")
elif resultatDau == 5:
    print("La cara oposada és el dos")
elif resultatDau == 6:
    print("La cara oposada és l'u")
elif resultatDau < 1 or resultatDau > 6:
    print("Error: Nombre incorrecte")
else:
    print("Error")