"""
Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros 
nomeados e imprime o valor de cada parâmetro recebido.

Teste sua função com os seguintes parâmetros:
(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

"""
# recebe um número variado de argumentos nomeados e não nomeados e os retorna em uma lista
def func(*args, **kwargs):
    p_args = []
    for i in args:
        p_args.append(i)

    # armazena somente os valores
    p_kwargs = []
    for key, value in kwargs.items():
        p_kwargs.append(value)
    
    # adiciona a lista p_kwargs ao fim da lista p_args
    p_args.extend(p_kwargs)
    
    return p_args

lista = func(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

for i in lista:
    print(i)