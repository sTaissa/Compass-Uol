"""
Escreva um código Python que imprime todos os números primos de 1 até 100.

"""
# retorna true se o número for primo e false se não for
# um número só é primo quando for divisível apenas por 1 e por ele mesmo
def primo(num):
    # 0, 1 ou negativos não são primos
    if num <= 1:
        return False

    # verifica se há alguma divisão exata por outro valor que não 1 ou o próprio número
    for i in range(2, num+1):
        if num % i == 0 and num != i:
            return False
    return True

# exibe todos os numero primos de 1 a 100
for i in range(1, 101):
    if primo(i):
        print(i)
    