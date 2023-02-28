"""
Escreve um código Python que lê do teclado o nome e a idade de um usuário e que imprime apenas o ano em que 
ele completará 100 anos.

"""
# importa biblioteca para trabalhar com datas
import datetime

# retorna qual o ano em que a idade informada vai completar 100 anos
def ano_100(idade):
    # calcula quantos anos faltam para completar 100 anos
    anos = 100 - idade

    # calcula qual o ano em que completará 100 anos, adicionando os anos faltantes (variável anos) à data atual
    # timedelta não aceita anos, então foi colocado dias 
    ano = datetime.datetime.now() + datetime.timedelta(days=anos*365)
    return ano.year

# le as variáveis e converte idade para int
nome = input('Informe seu nome: ')
idade = ''

while type(idade) != int:
    try:
        idade = int(input('Informe sua idade: '))
    except:
        print("Valor inválido, informe um número")

print(ano_100(idade))