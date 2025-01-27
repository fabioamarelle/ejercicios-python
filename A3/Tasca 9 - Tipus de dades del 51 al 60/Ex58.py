cerca = 0

# Llista amb tots els mesos de l'any
mesos = ["Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", "Agost", "Setembre", "Octubre", "Novembre", "Desembre"]
vectorIngressos = []

# Demana els ingressos per a cada mes de l'any
for i in range(12):
    ingressos = int(input(f"Introdueix la quantitat cobrada a {mesos[i]}: "))
    vectorIngressos.append(ingressos)

# Bucle fins que l'usuari introdueixi -1. Així permet fer més d'una cerca per execució.
while cerca != -1:
    cerca = int(input("Introdueix la quantitat d'ingressos a buscar. Introdueix -1 per sortir del programa: "))
    if cerca == -1:
        print("Sortint del programa.")
    elif not cerca in vectorIngressos: 
        print("Quantitat d'ingressos no trobada.")
    else:
        print(f"Ha cobrat aquesta quantitat a {mesos[vectorIngressos.index(cerca)]}")