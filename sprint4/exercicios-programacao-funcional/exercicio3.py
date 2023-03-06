"""
A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. Cada lançamento 
é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 

Abaixo apresentando uma possível entrada para a função.
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]
A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. Na lista anterior, 
por exemplo, teríamos como resultado final 200.

Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:
reduce (módulo functools)
map

"""

from functools import reduce 

def calcula_saldo(lancamentos) -> float:
    # usa map para criar uma lista com os valores da tupla, positivos se era 'C' e negativo se 'D'
    lista = list(map(lambda x: -x[0] if x[1] == 'D' else x[0], lancamentos))
    # retorna a soma de todos os valores da lista gerada
    return reduce(lambda x, y: x+y, lista)
