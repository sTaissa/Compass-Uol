"""
Criar novo script Python que implementa o algoritmo a seguir:

1 - Receber uma string via input
2 - Gerar o hash  da string por meio do algoritmo SHA-1
3 - Imprimir o hash em tela, utilizando o método hexdigest
4 - Retornar ao passo 1

"""
import hashlib

# usa hash sha1 para mascarar a palavra passado como parâmetro
def mascara(palavra):
    return hashlib.sha1(palavra.encode("utf-8")).hexdigest()

# exibe o resultado da função passada como parâmetro até que seja digitado "sair"
def repete(func):
    while True:
        str = input("Informe a expressão a ser mascarada ou 'sair': ")

        if str.lower() != "sair":
            print(func(str))
            print()
        else: 
            break

repete(mascara)