data = str(input("Introdueix una data (DD/MM/AAAA): "))
dia,mes,any = map(int, data.split('/'))                     # Separa la data DD/MM/AAAA en tres variables i les converteix a int, si no no es poden fer comprovacions

if dia > 31 or dia <= 0:
    print("El dia ha de ser un nombre entre 1 i 31.")
elif mes > 12 or mes <= 0:
    print("El mes ha de ser un nombre entre 1 i 12.")
elif any < 0:
    print("L'any no pot ser un nombre negatiu.")
else:
    print(f"La data {dia}/{mes}/{any} és correcta.")