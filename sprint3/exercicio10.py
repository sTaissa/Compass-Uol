"""
Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.

['abc', 'abc', 'abc', '123', 'abc', '123', '123']

"""
# transforma a lista em um conjunto para retirar elementos duplicados
def func(lista):
    return set(lista)

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

print(list(func(lista)))