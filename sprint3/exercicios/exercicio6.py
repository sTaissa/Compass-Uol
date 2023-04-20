"""
Dada duas listas como as no exemplo abaixo:
a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Escreva um programa que retorne o que ambas as listas têm em comum (sem repetições). O seu programa deve 
funcionar para listas de qualquer tamanho.

"""
# transforma as listas em conjuntos
a = set([1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89])
b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

# cria um novo conjunto com todos os valores correspondentes de 'a' e 'b'
c = a.intersection(b)
print(list(c))

