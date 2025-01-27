dia = int(input("Introdueix un dia: "))
mes = int(input("Introdueix un mes: "))
any = int(input("Introdueix un any: "))

mesos = ["gener", "febrer", "març", "abril", "maig", "juny", "juliol", "agost", "setembre", "octubre", "novembre", "desembre"]

if mes in [1,3,5,7,8,10,12]:
    diaMax = 31
elif mes in [4,6,9,11]:
    diaMax = 30
else:
    diaMax = 28

if dia > diaMax or dia <= 0:
    print(f"El dia ha de ser un nombre entre 1 i {diaMax}.")
elif mes > 12 or mes <= 0:
    print("El mes ha de ser un nombre entre 1 i 12.")




else:
    print(f"Data: {dia} de {mesos[mes-1]} de {any}")