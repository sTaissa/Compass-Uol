"""
Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!

import random 
# amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500),50)

Use as variáveis abaixo para representar cada operação matemática

mediana
media
valor_minimo 
valor_maximo 

"""
import random

# calcula a médiana da lista passada
# mediana é o valor central que separa a parte menor e maior de uma lista, então precisa ser ordenada
def func_mediana(lista):
    lista.sort()

    # se a lista for ímpar a mediana é o número do meio
    if len(lista) % 2 != 0:
        return lista[len(lista)//2]

    # se a lista for par a mediana é a média dos dois valores centrais
    else:
        valor_central1 = lista[len(lista)//2]
        valor_central2 = lista[(len(lista)//2) - 1]
        return func_media([valor_central1, valor_central2])

# calcula a média de todos os itens da lista
def func_media(lista):
    return sum(lista)/len(lista)

# retorna o valor mínimo da lista, comparando cada item com o menor valor achado até então
def func_min(lista):
    min = 501
    for i in lista:
        if i < min:
            min = i
    return min

# retorna o valor máximo da lista, comparando cada item com o maior valor achado até então
def func_max(lista):
    max = 0
    for i in lista:
        if i > max:
            max = i
    return max

# testa funções
random_list = random.sample(range(500), 50)

mediana = func_mediana(random_list)
media = func_media(random_list)
valor_minimo = func_min(random_list)
valor_maximo = func_max(random_list)

print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")