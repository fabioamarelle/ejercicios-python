# Activitat 1. Criptomonedes

# 1. Declaració de variables: Preu
btcPreu = 27000
ethPreu = 1800
xrpPreu = 0.50

# 1. Declaració de variables: Quantitat comprada
btcQuantitat = 0.5
ethQuantitat = 2
xrpQuantitat = 1000

# 2. Càlcul del valor total de la inversió
# Per saber el valor total s'han de multiplicar el preu i la quantitat de totes les criptomonedes i sumar-les.
valorTotal = (btcPreu * btcQuantitat) + (ethPreu * ethQuantitat) + (xrpPreu * xrpQuantitat)
print("2. Calcula el valor total de la criptomoneda")
print(f"El valor total de la inversió és {valorTotal}€.")

# 3. Càlcul del valor de cada criptomoneda
# Es fa un càlcul semblant a l'exercici 2, però separant cada criptomoneda en una variable diferent
btcValor = btcPreu * btcQuantitat
ethValor = ethPreu * ethQuantitat
xrpValor = xrpPreu * xrpQuantitat
print("3. Calcula el valor de cada criptomoneda")
print(f"El valor de la inversió en Bitcoin (BTC) és de {btcValor}€")
print(f"El valor de la inversió en Ethereum (ETH) és de {ethValor}€")
print(f"El valor de la inversió en Ripple (XRP) és de {xrpValor}€")

# 4. Càlcul del percentatge de cada criptomoneda respecte al valor total
# Per a calcular el percentatge s'utilitza la fòrmula "valorCriptomoneda / valorTotal * 100".
btcPercentatge = round((btcValor / valorTotal * 100),2)         # round() és una funció que permet arrodonir nombres, té el format round(nombre,decimals).
ethPercentatge = round((ethValor / valorTotal * 100),2)
xrpPercentatge = round((xrpValor / valorTotal * 100),2)
print("4. Calcula el percentatge de cada criptomoneda respecte al valor total")
print(f"Percentatge de Bitcoin (BTC): {btcPercentatge}%")
print(f"Percentatge de Ethereum (ETH): {ethPercentatge}%")
print(f"Percentatge de Ripple (XRP): {xrpPercentatge}%")

# 5. Càlcul del ROI
# La fòrmula utilitzada ja estava al Moodle: "((valorTotal - inversioInicial) / inversioInicial) * 100".
inversioInicial = 15000
roi = round((((valorTotal - inversioInicial) / inversioInicial ) * 100),2)
print("5. Calcula el ROI basat en una inversió inicial de 15.000€")
print(f"Rendiment de la inversió (ROI): {roi}%.")