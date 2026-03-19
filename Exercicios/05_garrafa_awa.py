# %%
texto = """ Escolha qual água você deseja comprar
(1)Água mineral natural 350ml
(2)Água mineral natural 500ml
(3)Água mineral natural 1L
(4)Água mineral com gás 350ml
(5)Água mineral com gás 500ml
(6)Água mineral com gás 1L
"""
opcao = input(texto)
if opcao == "1":
    print("Sua conta deu R$ 1,59.")
elif opcao == "2":
    print("Sua conta deu R$ 2,50.")
elif opcao == "3":
    print("Sua conta deu R$ 3.99.")
elif opcao == "4":
    print("Sua conta deu R$ 2,59.")
elif opcao == "5":
    print("Sua conta deu R$ 3,20.")
elif opcao == "6":
    print("Sua compra deu R$ 4,99.")
else:
    print("Opção invalida, tente novamente.")


# %%
