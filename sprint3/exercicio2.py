"""
Escreva um código Python que verifique se três números digitados pelo usuário são pares ou ímpares. Para cada 
número, imprima o Par: ou Ímpar: e o número correspondente.

Exemplo de formato de saída:
Par: 2
Ímpar: 3

"""
# retorna o número e se este é par ou ímpar
def impar_par(num):
    if num % 2 == 0:
        print("Par: " + str(num))
    else:
        print("Ímpar: " + str(num))

# solicita 3 números e chama a função que informa se é par ou impar
for i in range(3):
    num = input(f"Informe o numero {i+1}: ")
    impar_par(int(num))