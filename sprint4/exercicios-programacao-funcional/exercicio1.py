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
        return num


lista = extrai("sprint4/exercicios-programacao-funcional/number.txt")
# a divisão que dá 0 seria par, mas como 0 é false, dá o contrário
# o lambda inverte: quando a divisão der 1 (True) retorna False, se der 0 (False) retorna True
par = lambda x: False if x % 2 else True

# filtra(filter) somente os pares da lista, ordena(sorted) esse resultado em ordem decrescente(reverse=True) e pega somente os 5 primeiros valores([0:5])
res = list(sorted(filter(par, lista), reverse=True))[0:5]

print(res)
print(sum(res))
