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
lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

# transforma cada string em lista e verifica se esta fica igual de trás pra frente
for i in lista:
    item_lista = list(i)

    if item_lista == item_lista[::-1]:
        print("A palavra: " + i + " é um palíndromo")
    else:
        print("A palavra: " + i + " não é um palíndromo")