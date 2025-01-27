import random, string

# El mòdul string té constants amb totes les lletres i dígits.
caractersPossibles = string.ascii_letters + string.digits 

# random.choice tria un caràcter al atzar
nombreAleatori = f"{(random.choice(caractersPossibles))}{(random.choice(caractersPossibles))}{(random.choice(caractersPossibles))}"

print(nombreAleatori)