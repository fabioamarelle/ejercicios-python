npreguntesCorrectes = int(input("Nº Preguntes correctes: "))
npreguntesIncorrectes = int(input("Nº Preguntes incorrectes: "))
npreguntesBlanc = int(input("Nº Preguntes en blanc: "))
notaFinal = (npreguntesCorrectes * 5) + (npreguntesIncorrectes * -1)                # No es compten les preguntes en blanc
notaMaxima = (npreguntesCorrectes + npreguntesIncorrectes + npreguntesBlanc) * 5    # La quantitat màxima de punts és el nombre de preguntes multiplicada per 5

print(f"La teva nota final és de {notaFinal}/{notaMaxima}.")