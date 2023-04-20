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
        return "Par"
    else:
        return "Ímpar"

# solicita 3 números e chama a função que informa se é par ou impar
for i in range(3):
    num = ''
    while type(num) != int:
        try:
            num = int(input(f"Informe o numero {i+1}: "))
        except:
            print("Valor inválido, informe um número")
    print(impar_par(num) + ": " + str(num))
    