#%%
soma = 0 

qntd_entrada = 4

for i in range(qntd_entrada):
    altura = input("Informe a sua altura: ")
    altura = float(altura)
    soma += altura
  
print("Soma das alturas: ", soma)