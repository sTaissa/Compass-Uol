# extrai os dados do arquivo csv, tranforma em uma lista de dicionários python e limpa/padroniza os dados
def extrai():
    # abre o arquivo em forma de string
    with open("sprint3/desafio/actors.csv", "r", encoding="utf8") as file:
        lista = []
        contador = 0

        # lê cada linha do arquivo
        for line in file.readlines():
            ator = {}
            # ignora a primeira linha (cabeçalho do csv)
            if contador == 0:
                contador += 1
                continue

            # transforma cada linha em uma lista
            item = line.split(",")

            # trata casos em que há ',' a mais além das usadas para separação de dados (6)
            # se houverem mais, o split anterior retornará mais do que 6 dados
            if len(item) > 6:
                # separa o item com a ',' a mais, que está envolto em aspas duplas
                item_diferente = line.split('"')
                # retira a ',' e unifica as divisões por aspas feitas anteriormente
                novo = item_diferente[1].replace(",", "") + item_diferente[2]
                # divide a string agora no padrão das outras em uma lista
                item = novo.split(",")

            # retira espaços vazios no começo e final de cada item
            for i in item:
                i.strip()

            # armazena cada item da linha em um dicionário para ficar mais entendível
            ator['nome'] = item[0]
            ator['total'] = float(item[1])
            ator['filmes'] = int(item[2])
            ator['media'] = float(item[3])
            ator['1 filme'] = item[4]
            ator['bruto'] = float(item[5])

            # adiciona cada dicionário com os dados do ator em uma lista para ter todos os dados
            lista.append(ator)
        file.close()
    return lista

# retorna o ator com maior número de filmes e o respectivo número
def mais_filmes(dados):
    maior = 0
    for item in dados:
        if item['filmes'] > maior:
            maior = item['filmes']
            ator = item['nome']
    return ator, maior

# retorna a média do número de filmes por autor
def media_filmes(dados):
    soma = 0
    for ator in dados:
        soma += ator['filmes']
    return soma/len(dados)

# retorna o ator com a maior média por filme
def maior_media(dados):
    maior = 0
    for item in dados:
        if item['media'] > maior:
            maior = item['media']
            ator = item['nome']
    return ator

# exetuta funções
ator, filmes = mais_filmes(extrai())
#print(f"Ator/atriz com maior número de filmes: {ator}. Quantidade de filmes: {filmes}")

#print(f"A média do número de filmes por autor é: {media_filmes(extrai())}")

print(f"Ator/atriz com a maior média por filme: {maior_media(extrai())}")

