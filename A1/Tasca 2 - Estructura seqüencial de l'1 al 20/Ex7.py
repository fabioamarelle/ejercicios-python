minuts = int(input("Introdueix el valor (en minuts): "))
hores = minuts // 60    # Divideix, eliminant el residu (minuts)
residu = minuts % 60    # Calcula el residu, que en aquest cas són els minuts sobrants 
print(f"{minuts} minuts són {hores} hores i {residu} minuts")