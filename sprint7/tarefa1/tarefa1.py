# extrai os dados do arquivo
import pandas as pd
def extrai():
    actors = pd.read_csv("sprint7/tarefa1/actors.csv", sep=",")
    return actors

# 1- Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes
def mais_filmes(dados):
    # identifica o ator (ou atores caso haja mais de um) com o maior número de filmes
    maiores = dados.nlargest(1, "Number of Movies", keep="all")
    ator = maiores['Actor'].values
    filmes = maiores['Number of Movies'].values

    # printa os valores pedidos
    print("Exercício 1")
    for nome in ator:
        print("O ator/atriz com maior número de filmes é {} com {} filmes".format(nome, str(filmes[0])))
    
    print()

    # retorna o dataframe com o nome e número de filmes para possível uso
    return maiores[['Actor', 'Number of Movies']]

# 2- Apresente a média da coluna contendo o número de filmes
def media_filmes(dados):
    media = dados['Number of Movies'].mean()

    # printa os valores pedidos
    print("Exercício 2")
    print("A média do número de filmes é:", media, "\n")

    return media    

# 3- Apresente o nome do ator/atriz com a maior média por filme
def maior_media(dados):
    # identifica o ator (ou atores) com a maior média por filme
    maiores = dados.nlargest(1, "Average per Movie", keep="all")
    ator = maiores['Actor'].values

    print("Exercício 3")
    for nome in ator:
        print("O ator/atriz com maior média por filme é", nome)
    
    print()
    # retorna a linha com o nome do ator 
    return ator

# 4- Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência
def filme_frequente(dados):
    # conta a quantidade de vezes que cada filme aparece, já em ordem decrescente
    freq = dados['#1 Movie'].value_counts()

    # exibe os dados no formato pedido
    print("Exercício 4")
    c = 1
    for filme, f in freq.items():
        print("{} - O filme {} aparece {} vez(es) no dataset".format(c, filme, f))
        c += 1
    return freq

    

dados = extrai()
mais_filmes(dados)
media_filmes(dados)
maior_media(dados)
filme_frequente(dados)