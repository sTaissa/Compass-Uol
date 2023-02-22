"""
Escreva um código Python que tem 3 variáveis dia (22), mês(10) e ano(2022) e imprime a data completa no formato a seguir:
Exemplo: 22/10/2022

Importante: É necessário formatar as variáveis como strings antes de concatená-las e imprimi-las na tela.

"""
import datetime

dia = 22
mes = 10
ano = 2022

# transforma as variaveis para o tipo datetime
data = datetime.datetime(ano, mes, dia)

#formata a data para o formato que usamos no Brasil
data_formatada = data.strftime('%d/%m/%Y')

print(data_formatada)

"""
Se apenas concatenar as variáveis em uma string dá certo na Udemy também:

dia = 22
mes = 10
ano = 2022

print(f"{str(dia)}/{str(mes)}/{str(ano)}")

"""