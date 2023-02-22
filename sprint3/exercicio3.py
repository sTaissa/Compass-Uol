"""
Escreva um código Python que imprime os números pares de 0 até 20 (incluso).

"""
# range(21) para que o 20 seja incluso
for i in range(21):
    if i % 2 == 0:
        print(i)
    