# %%    

valor = """Seja bem-vindo! Qual tipo de sorvete você deseja? 
(1)Casquinha que está por R$2,50, 
(2)Cascão que está saindo por R$4,60 
(3)Cestinha que está no valor de R$6,00
"""

opcao = input(valor)

tipo_sorv = 0
if opcao == "1":
    tipo_sorv = 2.5
elif opcao == "2":
    tipo_sorv = 4.6
elif opcao == "3":
    tipo_sorv = 6.9
else:
    print("Só trabalhamos com esses tipos de casquinhas.")

texto = """Qual sabor você deseja?
(1) Morango
(2) Creme
(3)Chocolate
(4)Meio a Meio(Chocolate/Creme)
"""

sabor = input(texto)
if sabor == "1":
    print("Certo então será sabor morango")
elif sabor == "2":
    print("Certo então será sabor creme")
elif sabor == "3":
    print("Certo então será sabor chocolate")
elif sabor == "4":
    print("Certo então será sabor meio a meio")
else:
    print("Só trabalhamos com esses sabores de sorvete.")

menu_cobertura = """Os valores das coberturas são:
(1)Caramelo - R$1,50
(2)Morango - R$1,50
(3)Chocolate - R$1,50
(4)Sem cobertura - R$0,00
"""

tipo = input(menu_cobertura)

valor_cobertura = 0 

if tipo == "1":
    valor_cobertura = 1.5
elif tipo == "2":
    valor_cobertura = 1.5
elif tipo == "3":
    valor_cobertura = 1.5
elif tipo == "4":
    valor_cobertura = 0
else:
    print("Só trabalhamos com esses sabores de cobertura.")

# Agora a soma é feita com segurança!
valor_total = tipo_sorv + valor_cobertura
print(f"Deu no total: R$ {valor_total:.2f}".replace('.', ','))

# %%
