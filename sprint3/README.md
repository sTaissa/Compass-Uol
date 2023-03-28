<h1 align="center"> Sprint 3</h1>

<p align="center">
 <a href="#sobre">Sobre</a> •
 <a href="#exercicios">Exercícios Python</a> •
 <a href="#desafio">Desafio de ETL Python</a>
</p>

<br> 

<a id="sobre"></a>
## 📎 Sobre

### Mentor

[Matheus Toledo](https://github.com/toledkrw)

### Cursos
- [Programação em Python do básico ao avançado](https://www.udemy.com/course/curso-de-programacao-em-python-do-basico-ao-avancado/) (Apenas uma parte do curso)

### Anotações
- [Anotações sobre Python](https://lowly-pear-52e.notion.site/Python-a4660e09cb7b48b789d7f56407281078)

<br>

<a id="exercicios"></a>
## 🐍 Exercícios Python

<br>

[Link](/sprint3/exercicios/) para os 25 exercícios

<br>

<a id="desafio"></a>
##  📥  Desafio ETL Python

<br>

>Armazene o arquivo [actors.csv](/sprint3/desafio/actors.csv) dentro de uma nova pasta, após isso crie 5 arquivos do tipo “txt” vazios (1 para cada exercício do desafio).

>Em seguida para cada uma das tarefas da sequencia, leia o arquivo actors.csv utilizando Python como linguagem de programação e depois de obter as repostas necessárias armazene cada um dos resultados em um dos arquivos “txt” criados.

>Pontos de Atenção:
>- Para desenvolvimento deste exercício, **não deve ser** utilizado as bibliotecas Pandas e NumPy e/ou outras bibliotecas e engines que utilizam de dataframes.
>- Todas as transformações que julgarem necessárias, devem ser feitas utilizando os scripts Python e **nenhuma modificação deve ser feita no arquivo actors.csv**
>- Para leitura do arquivo actors.csv, **não deve** ser utilizado o módulo csv nativo do Python.

---

[Código completo do desafio](/sprint3/desafio/ETL.py)

### Extração e Transformação
Como não podemos usar o módulo csv do Python, transformei cada linha do arquivo csv em um dicionário e coloquei todos em uma lista

``` Python
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
```

### Exercício 1
O ator/atriz com maior número de filmes e o respectivo número de filmes
``` Python
# recebe os dados extraídos e transformados
def mais_filmes(dados):
    ator, numero = maior(dados, 'filmes')
    
    # armazena o resultado em um novo arquivo
    with open("sprint3/desafio/desafio1.txt", "w", encoding="utf-8") as file:
        file.write("O ator/atriz com maior número de filmes e o respectivo número de filmes:\n\n")
        file.write(f"{ator}, {numero} filmes")
        file.close()

    return ator, maior
```

Função usada para achar o maior valor na questão 1 e 3:
``` Python
def maior(lista, dado):
    maior = 0
    for item in lista:
        if item[dado] > maior:
            maior = item[dado]
            ator = item['nome']
    return ator, maior
```
[Arquivo](/sprint3/desafio/desafio1.txt) gerado:

![desafio1](/sprint3/imagens-sprint3/desafio1.PNG)

### Exercício 2
A média do número de filmes por autor
``` Python
# recebe os dados extraídos e transformados
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
```
[Arquivo](/sprint3/desafio/desafio2.txt) gerado:

![desafio2](/sprint3/imagens-sprint3/desafio2.PNG)

### Exercício 3
O ator/atriz com a maior média por filme
``` Python
# recebe os dados extraídos e transformados
def maior_media(dados):
    ator, maior_media = maior(dados, 'media')

    # armazena o resultado em um novo arquivo
    with open("sprint3/desafio/desafio3.txt", "w", encoding="utf-8") as file:
        file.write("O ator/atriz com a maior média por filme:\n\n")
        file.write(ator)
        file.close()

    return ator
```
[Arquivo](/sprint3/desafio/desafio3.txt) gerado:

![desafio3](/sprint3/imagens-sprint3/desafio3.PNG)

### Exercício 4
O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência
``` Python
# recebe os dados extraídos e transformados
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
```
[Arquivo](/sprint3/desafio/desafio4.txt) gerado:

![desafio4](/sprint3/imagens-sprint3/desafio4.PNG)

### Exercício 5
A lista dos Autores ordenada por pagamento. Do mais bem pago para o menos bem pago
``` Python
# recebe os dados extraídos e transformados
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
```
[Arquivo](/sprint3/desafio/desafio5.txt) gerado:

![desafio5.1](/sprint3/imagens-sprint3/desafio5.1.PNG)
![desafio5.2](/sprint3/imagens-sprint3/desafio5.2.PNG)
