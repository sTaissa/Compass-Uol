"""
Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e o 
resultado deverá ser a contagem de vogais presentes em seu conteúdo.

É obrigatório aplicar as seguintes funções:
len
filter
lambda

Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.

"""
def conta_vogais(texto:str)-> int:
    vogais = lambda x: x in ['a', 'e', 'i', 'o', 'u']
    # filtra as vogais da string e retorna o tamanho da lista gerada pela filtragem 
    return len(list(filter(vogais, texto.lower())))