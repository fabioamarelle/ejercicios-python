A = int(input("Introdueix el primer nombre (A): "))
B = int(input("Introdueix el segon nombre (B): "))

temp = B
B = A
A = temp

print(f"A = {A}")
print(f"B = {B}")