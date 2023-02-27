"""
Dada as listas a seguir:

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".
Exemplo:
0 - João Soares está com 19 anos
"""
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

# agrupa os dados em uma tupla por pessoa
lista = list(zip(primeirosNomes, sobreNomes, idades))

# enumera cada tupla de dados da pessoa
for i, pessoa in enumerate(lista):
    print(f"{i} - {pessoa[0]} {pessoa[1]} está com {pessoa[2]} anos")
