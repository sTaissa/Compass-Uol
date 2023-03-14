"""
A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. Em operadores, espera-se 
uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %), as quais devem ser aplicadas 
à lista de operadores nas respectivas posições. Após aplicar cada operação ao respectivo par de operandos, a função deverá 
retornar o maior valor dentre eles.

Veja o exemplo:

Entrada
operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

Aplicar as operações aos pares de operandos
[ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ] 

Obter o maior dos valores
12

Na resolução da atividade você deverá aplicar as seguintes funções:
max
zip
map

"""
def calcular_valor_maximo(operadores,operandos):
    # função a ser executada no map
    # eval calcula a operação passada em string
    operacao = lambda x: eval(f"{x[1][0]} {x[0]} {x[1][1]}")

    # junta os operadores com operandos através do 'zip', e usa essa lista para fazer os calculos com map
    return max(list(map(operacao, list(zip(operadores, operandos)))))

