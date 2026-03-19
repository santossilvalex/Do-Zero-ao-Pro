# %%
lista = [1,2,3,4,5,1,6,7,8,9,1,1,1,3,4,5,6,7,8,1,4,1,5]

numero = input("Digite um número: ")
numero = int(numero)

contato = 0
for i in lista:
    if i == numero:
        contato += 1
print("Quantidade de", numero, "na lista:", contato)

# %%
