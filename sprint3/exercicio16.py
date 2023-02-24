"""
Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. 
Depois imprima a soma dos valores.
A string deve ter valor  "1,3,4,6,10,76"
"""
# recebe uma string, separa em uma lista e retorna a soma de seus item
def soma_string(string):
    lista = string.split(",")

    soma = 0
    for i in lista:
        soma += int(i)
    return soma

# testa a funcao
string = "1,3,4,6,10,76"

print(soma_string(string))