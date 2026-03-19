# %%
texto = """ Escolha qual água você deseja comprar
(1)Água mineral natural 350ml - R$1,50
(2)Água mineral natural 500ml - R$1,90
(3)Água mineral natural 1L - R$3,50
(4)Água mineral com gás 350ml - R$2,40
(5)Água mineral com gás 500ml - R$3,20
(6)Água mineral com gás 1L - R$4,10
"""
opcao = input(texto)

valor_item = 0
if opcao == "1":
    valor_item = 1.5
elif opcao == "2":
    valor_item = 1.9
elif opcao == "3":
    valor_item = 3.5
elif opcao == "4":
    valor_item = 2.4
elif opcao == "5":
    valor_item = 3.2
elif opcao == "6":
    valor_item = 4.1


if valor_item == 0:
    print("Opção invalida, tente novamente.")

else:
    qtde = input("Quantas garrafas você deseja levar? ")
    qtde = int(qtde)
    valor_total = valor_item * qtde
    print("Sua conta deu: R$", valor_total)


# %%
