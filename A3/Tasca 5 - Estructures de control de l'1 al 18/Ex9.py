a = int(input("Introdueix el primer nombre: "))
b = int(input("Introdueix el segon nombre: "))
c = int(input("Introdueix el tercer nombre: "))

# Hi ha 6 casos posibles 
# a b c, c b a, b a c, b c a, a c b, c a b

# Casos ón A és el nombre més gran
if a >= b and a >= c:
    if b >= c:
        ordre = [a, b, c]
    else:
        ordre = [a, c, b]
# Casos ón B és el nombre més gran
elif b >= a and b >= c:
    if a >= c:
        ordre = [b, a, c]
    else:
        ordre = [b, c, a]
# Casos ón C és el nombre més gran
else:
    if a >= b:
        ordre = [c, a, b]
    else:
        ordre = [c, b, a]

print(f"Nombres ordenats: {ordre}.")