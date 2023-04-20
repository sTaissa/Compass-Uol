"""
Dada a seguinte lista:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Faça um programa que gere uma nova lista contendo apenas números ímpares.

"""
# recebe uma lista e retorna outra apenas com os valores ímpares da primeira
def lista_impar(lista):
    b = []

    for i in lista:
        if i % 2 != 0:
            b.append(i)
    return b

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(lista_impar(a))