"""
Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros 
nomeados e imprime o valor de cada parâmetro recebido.

Teste sua função com os seguintes parâmetros:
(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

"""
# recebe um número variado de argumentos nomeados e não nomeados e os imprime
def func(*args, **kwargs):
    for i in args:
        print(i)
    # imprime somente os valores
    for key, value in kwargs.items():
        print(value)

func(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)