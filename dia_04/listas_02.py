# %%
alex = ["Alexsander", 27, 
        1.73, "Namorando",
        ["Desempregado", "Estudante"],
        ["RPG", "Games", "Musicas"]
    ]
print("Tamanho de Alex:", len(alex))

alex[5][1]
# %%
tamanho_lista = len(alex)
pos = tamanho_lista - 1

atividades = alex[pos]

alex[pos][len(atividades) - 1]
# %%
