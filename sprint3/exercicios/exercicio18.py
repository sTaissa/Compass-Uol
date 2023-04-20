"""
Dado o dicionário a seguir:
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.
"""
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

# transforma os valores do dicionário em uma lista
lista = []
for key, value in speed.items():
    lista.append(value)

# transforma a lista dos valores em conjunto para retirar valores duplicados
lista = set(lista)
# transforma o conjunto em lista novamente e exibe na tela
print(list(lista))
