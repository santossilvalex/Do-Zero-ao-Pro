# %%

def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    '''juros_compostos(serve para calcular o retorno financeiro de um investimento com juros compostos, 
    lembrando que deve considerar sempre o valor do juros atua e o tempo de que deseja manter o dinheiro investido.)
    
    aporte: 
        valor inicial investido 
    taxa: 
        taxa de juros em decimal (ex: 10% = 0.1) 
    anos: 
        tempo em anos que o dinheiro ficará investido 
    '''
    return aporte * (1 + taxa) ** anos
# %%
juros_compostos(aporte=2000, taxa=1, anos=5)
# %%
print()
