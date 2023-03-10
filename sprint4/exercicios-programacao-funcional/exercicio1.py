"""
Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, 
apresente os 5 maiores valores pares e a soma destes.

Você deverá aplicar as seguintes funções no exercício:
map
filter
sorted
sum

Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
a lista dos 5 maiores números pares em ordem decrescente;
a soma destes valores.

"""
# extrai os dados do arquivo e joga numa lista de int
def extrai(caminho):
    with open(caminho) as file:
        num = file.read().split("\n")
        num = list(map(lambda x: int(x), num))
        file.close()

    def filtra():
        par = lambda x: x % 2 == 0

        # filtra(filter) somente os pares da lista, ordena(sorted) esse resultado em ordem decrescente(reverse=True) e pega somente os 5 primeiros valores([0:5])
        return list(sorted(filter(par, num), reverse=True))[0:5]
    
    return filtra()


lista = extrai("sprint4/exercicios-programacao-funcional/number.txt")

print(lista)
print(sum(lista))
