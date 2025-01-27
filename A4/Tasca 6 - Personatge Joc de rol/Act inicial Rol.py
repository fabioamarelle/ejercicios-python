def crearPersonatge():
    personatge = {
                    "Nom": "Eldran",
                    "Classe": "Guerrer",
                    "Nivell": 5,
                    "Vida": 100,
                    "Inventari": ["Espasa", "Escut", "Poció de vida"]
                  }
    return personatge

def accedirPersonatge(personatge):
    print("─" * 75)
    print("Dades del personatge")
    print(f"Nom: {personatge["Nom"]}")
    print(f"Vida: {personatge["Vida"]}")
    print(f"Classe: {personatge.get("Classe", "Desconegut")}")
    print(f"Objecte: {personatge.get("Inventari", "Desconegut")[0]}")
    print(f"Inventari: {personatge.get("Inventari", "Desconegut")}")
    print("─" * 75)


def modificarPersonatge(personatge):
    print(f"{personatge.get("Nom")} ha pujat de nivell.")
    # Modifica les dades
    personatge["Nivell"] += 1
    personatge["Vida"] = 75
    personatge["Inventari"].append("Anell màgic")
    personatge["Classe"] = "Paladí"

    print("Mostrant noves estadístiques.")
    accedirPersonatge(personatge)

    return personatge

def utilitzarPocio(personatge):
    print("Poció utilitzada")
    personatge["Vida"] += 25
    personatge["Inventari"].remove("Poció de vida")
    print(f"Vida: {personatge.get("Vida", "Desconegut")}")
    print("─" * 75)
    return personatge

def eliminarPersonatge(personatge):
    personatge = utilitzarPocio(personatge)

    classe_eliminada = personatge.pop("Classe")
    print(f"Classe eliminada: {classe_eliminada}")
    
    ultimElement = personatge.popitem()
    print(f"Últim element (eliminat del diccionari): {ultimElement}")

    personatge.clear()
    print(personatge)

    return personatge


personatge = crearPersonatge()
accedirPersonatge(personatge)
personatge = modificarPersonatge(personatge)
personatge = eliminarPersonatge(personatge)

