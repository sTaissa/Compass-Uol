"""
Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes 
iguais. Teste sua implementação com a lista abaixo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

"""
def tres_listas(lista):
    # se a lista puder ser dividida em 3 partes, retorna as 3
    if len(lista) % 3 == 0:
        n = len(lista)//3
        l1 = lista[:n]
        l2 = lista[n:(n*2)]
        l3 = lista[(n*2):]
        return l1, l2, l3
    # se não puder, avisa isso e retorna o mais próximo de 3 partes iguais
    else: 
        print("Não é possível dividir a lista em 3 partes iguais")
        n = round(len(lista)/3)
        l1 = lista[:n]
        l2 = lista[n:(n*2)]
        l3 = lista[(n*2):]
        return l1, l2, l3

# testa a função
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

listas = tres_listas(lista)
print(listas[0], listas[1], listas[2])
