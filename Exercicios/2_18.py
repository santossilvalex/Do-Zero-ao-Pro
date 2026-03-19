
frases = {}

while True:
    frase = input ("Digite uma frase:")
    if frase == "":
        break

    if frase not in frases:
        frases[frase] = 1
    else:
        frases[frase] += 1
for frase, quantidade in frases.items():
    print(f'A frase "{frase}" foi digitada {quantidade} vezes.')