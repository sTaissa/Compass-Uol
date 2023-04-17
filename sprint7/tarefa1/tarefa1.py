# extrai os dados do arquivo
import pandas as pd
def extrai():
    actors = pd.read_csv("sprint7/tarefa1/actors.csv", sep=",")
    return actors

# 1- Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes
def mais_filmes(dados):
    # identifica o ator (ou atores) com o maior número de filmes
    maiores = dados.nlargest(1, "Number of Movies", keep="all")
    ator = maiores['Actor'].values
    filmes = maiores['Number of Movies'].values

    # printa os valores pedidos
    print("Exercício 1")
    print("Ator com maior número de filmes: ", end='')
    for nome in ator:
        print(nome)
    print("Número de filmes:", filmes[0], "\n")

    # retorna o dataframe com o nome e número de filmes para possível uso
    return maiores[['Actor', 'Number of Movies']]

# 2- Apresente a média da coluna contendo o número de filmes
def media_filmes(dados):
    media = dados['Number of Movies'].mean()

    # printa os valores pedidos
    print("Exercício 2")
    print("Média do número de filmes dos atores:", media, "\n")

    return media    

# 3- Apresente o nome do ator/atriz com a maior média por filme
def maior_media(dados):
    # identifica o ator (ou atores) com a maior média por filme
    maiores = dados.nlargest(1, "Average per Movie", keep="all")
    ator = maiores['Actor'].values

    print("Exercício 3")
    print("Ator com maior média por filme: ", end='')
    for nome in ator:
        print(nome)
    print()
    # retorna a linha com o nome do ator 
    return ator

# 4- Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência
def filme_frequente(dados):
    # agrupa pela coluna '#1 Movie', o filme (ou filmes) que tiver maior contagem de atores é o mais frequente
    freq = dados.groupby('#1 Movie').count()
    maiores = freq.nlargest(1, "Actor", keep="all")
    filme = maiores['Actor']

    print("Exercício 4")
    print("Filme mais frequente: ", end='')
    for freq in filme.index:
        print(freq)
    print("Frequência:", filme[0])
    return filme

    

dados = extrai()
mais_filmes(dados)
media_filmes(dados)
maior_media(dados)
filme_frequente(dados)