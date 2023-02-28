"""
Cada função cria um novo arquivo com os dados obtidos e retorna os mesmos dados para eventual utilização no programa

"""

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


# desafio 1
# retorna o ator com maior número de filmes e o respectivo número
def mais_filmes(dados):
    ator, numero = maior(dados, 'filmes')
    
    # armazena o resultado em um novo arquivo
    with open("sprint3/desafio/desafio1.txt", "w", encoding="utf-8") as file:
        file.write("O ator/atriz com maior número de filmes e o respectivo número de filmes:\n\n")
        file.write("Ator, Número de filmes\n")
        for nome in ator:
            file.write(f"{nome}, {numero}")
        file.close()

    return ator, numero


# desafio 2
# retorna a média do número de filmes por autor
def media_filmes(dados):
    soma = 0
    for ator in dados:
        soma += ator['filmes']
    media = soma / len(dados)

    # armazena o resultado em um novo arquivo
    with open("sprint3/desafio/desafio2.txt", "w", encoding="utf-8") as file:
        file.write("A média do número de filmes por autor:\n\n")
        file.write(str(media))
        file.close()

    return media


# desafio 3
# retorna o ator com a maior média por filme
def maior_media(dados):
    ator, maior_media = maior(dados, 'media')

    # armazena o resultado em um novo arquivo
    with open("sprint3/desafio/desafio3.txt", "w", encoding="utf-8") as file:
        file.write("O ator/atriz com a maior média por filme:\n\n")
        for nome in ator:
            file.write(nome)
        file.close()

    return ator


# desafio 4
# retorna uma lista com o(s) filme(s) que mais aparece(m) e sua frequência
def filme_frequente(dados):
    # cria um dicionário com cada filme individual e a sua frequência
    filmes = {}
    for item in dados:
        # se o filme não estiver no dicionário, adiciona, se já estiver, apenas incrementa sua frequência
        if item['1 filme'] not in filmes:
            filmes[item['1 filme']] = 1
        else:
            filmes[item['1 filme']] += 1
    
    # verifica qual o filme/filmes do dicionário com maior frequência
    maior_frequencia = 0
    frequente = []
    for filme, frequencia in filmes.items():
        # se for encontrada uma frequência maior, limpa a lista e adiciona o filme com a maior frequência apenas
        if frequencia > maior_frequencia:
            maior_frequencia = frequencia
            frequente = []
            frequente.append(filme)
        # se houver mais de 1 filme com a maior frequência atual, adiciona este à lista de filmes com maior frequência
        elif frequencia == maior_frequencia:
            frequente.append(filme)

    # armazena o resultado em um novo arquivo
    with open("sprint3/desafio/desafio4.txt", "w", encoding="utf-8") as file:
        file.write("O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência:\n\n")
        file.write("Filme, Frequência\n")
        for filme in frequente:
            file.write(f"{filme}, {maior_frequencia}")
        file.close()

    return frequente, maior_frequencia


    resposta = ""
    c = 0
    for i in lista:
        # se for o último item da lista não coloca vírgula ao fim
        if c != len(lista) - 1:
            resposta += i + ", "
        else:
            resposta += i
        c += 1
    return resposta


# desafio 5
# retorna uma lista dos autores, do mais bem pago para o menos bem pago
def autores_salario(dados):
    # cria um dicionário com cada autor e seu pagamento
    pagamento = {}
    for i in dados:
        pagamento[i['nome']] = i['total']
    
    # ordena o dicionário pelo maior pagamento e adiciona em uma lista apenas o nome do autor
    autores = []
    for i in sorted(pagamento, key=pagamento.get, reverse=True):
        autores.append(i)

    # armazena o resultado em um novo arquivo
    with open("sprint3/desafio/desafio5.txt", "w", encoding="utf-8") as file:
        file.write("A lista dos Autores ordenada por pagamento. Do mais bem pago para o menos bem pago:\n\n")
        for autor in autores:
            file.write(autor + "\n")
        file.close()

    return autores

# retorna o maior valor, ou maiores valores de acordo com o dado passado e a qual ator pertence esse valor
# evita repetição de código em outras funções
def maior(lista, dado):
    maior = 0
    nome = []
    for item in lista:
        # se for encontrada um dado maior, limpa a lista e adiciona o ator com o maior dado apenas
        if item[dado] > maior:
            maior = item[dado]
            nome = []
            nome.append(item['nome'])
        # se tiver mais de um dado com o maior valor atual, adiciona o ator a que pertence esse dado à lista de nomes
        elif item[dado] == maior:
            nome.append(item['nome'])
    return nome, maior

# executa funções
dados = extrai()
mais_filmes(dados)
media_filmes(dados)
maior_media(dados)
filme_frequente(dados)
autores_salario(dados)