"""
Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.
Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.

É necessário que você imprima no console exatamente assim:
A palavra: maça não é um palíndromo
A palavra: arara é um palíndromo
A palavra: audio não é um palíndromo
A palavra: radio não é um palíndromo
A palavra: radar é um palíndromo
A palavra: moto não é um palíndromo

"""
# recebe uma lista e retorna-a invertida
def inverte(lista):
    j = -1
    for i in range(0, len(lista)//2):
        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp
        j += j
    return lista

lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for i in lista:
    item_lista = list(i)
    item_reverse = inverte(item_lista)

    if item_lista == item_reverse:
        print("A palavra: " + i + " é um palíndromo")
    else:
        print("A palavra: " + i + " não é um palíndromo")