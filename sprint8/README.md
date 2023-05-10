<h1 align="center"> Sprint 8</h1>

<p align="center">
 <a href="#sobre">Sobre</a> •
 <a href="#tarefa1">Tarefa 1</a> •
 <a href="#desafio">Desafio parte 2</a> •
 <a href="#tarefa3">Tarefa 3</a> •
 <a href="#tarefa4">Tarefa 4</a>
</p>

<br> 

<a id="sobre"></a>
## 📎 Sobre

### Mentor

Mateus Presotto Balen

### Cursos
- [Formação Spark com Pyspark : o Curso Completo](https://www.udemy.com/course/spark-curso-completo/?utm_source=adwords-intl&utm_medium=udemyads&utm_campaign=LongTail_new_la.PT_cc.BR&utm_content=deal4584&utm_term=_._ag_118044111562_._kw__._ad_491671393399_._de_c_._dm__._pl__._ti_dsa-1131315795548_._li_9047798_._pd__._&gclid=CjwKCAjw9J2iBhBPEiwAErwpeZ-3bys18AOcblMFlQx3eJjdpBRz-8hp3mNwFIBs8nod1muxs1X40RoC96QQAvD_BwE)


### Anotações
- [Spark e Pyspark](https://lowly-pear-52e.notion.site/Spark-e-PySpark-b238560dafbb45768d177de12359854a)

<br>

<a id="tarefa1"></a>
## 📋 Tarefa 1 - Exercício TMDB

>Será preciso criar uma conta no portal do TMDB para, após, solicitar as chaves de acesso para uso da API

> Uma vez que você tenha sua chave de API, você pode fazer solicitações à API, teste suas credenciais com base no código de exemplo abaixo:
>```Python
>import requests
>import pandas as pd
>
>from IPython.display import display
>
>api_key = "SUA CHAVE"
>
>url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"
>
>response = requests.get(url)
>data = response.json()
>
>filmes = []
>
>for movie in data['results']:
>    df = {'Titulo': movie['title'],
>    'Data de lançamento': movie['release_date'],
>    'Visão geral': movie['overview'],
>    'Votos': movie['vote_count'],
>    'Média de votos:': movie['vote_average']}
>    filmes.append(df)
>
>df = pd.DataFrame(filmes)
>display(df)
> ```

Clique para conferir: [meu código](/sprint8/tarefa1/tbmd-teste.py)

<br>

<a id="desafio"></a>
## 📤 Tarefa 2 - Desafio parte 2 - Ingestão de dados do Twitter e/ou TMBD

Temos um desafio final para entregar ao fim do programa, nessa sprint realizamos a segunda parte dele, acesse: [desafio](/desafio/)

<br>

<a id="tarefa3"></a>
## 🗃️  Tarefa 3 - Exercícios - Geração de massa de dados

Confira o notebook com todos os códigos e resultados: [notebook](/sprint8/tarefa3/gera-dados.ipynb)

>1. [Warm up]  Em Python, declare e inicialize uma lista contendo 250 inteiros obtidos de forma aleatória. Após, aplicar o método reverse sobre o conteúdo da lista e imprimir o resultado.

>2. [Warm up] Em Python, declare e inicialize uma lista contendo o nome de 20 animais. Ordene-os em ordem crescente e itere sobre os itens, imprimindo um a um (você pode utilizar list comprehension aqui).  Na sequência, armazene o conteúdo da lista em um arquivo de texto, um item em cada linha, no formato CSV.

Acesse o arquivo gerado pelo código: [csv](/sprint8/tarefa3/animais.csv)

>3. [Laboratório] Elaborar um código Python para gerar um dataset de nomes de pessoas. Siga os passos a seguir para realizar a atividade:
>
>Passo 1:  Instalar biblioteca names para geração de nomes aleatórios. O comando de instalação é pip install names
>
>Passo 2 Importar as bibliotecas random, time, os e names em seu código
>
>Passo 3: Definir os parâmetros para geração do dataset, ou seja, a quantidades de nomes aleatórios e a quantidade de nomes que devem ser únicos.
>``` Python
># Define a semente de aleatoriedade
>random.seed(40)
>
>qtd_nomes_unicos = 3000
>
>qtd_nomes_aleatorios = 10000000
>```
>
>Passo 4: Gerar os nomes aleatórios.
>``` Python
>aux=[]
>for i in range(0, qtd_nomes_unicos):
>    aux.append(names.get_full_name())
>
>print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))
>
>dados=[]
>for i in range(0,qtd_nomes_aleatorios):
>    dados.append(random.choice(aux))
>```
>
>Passo 5: Gerar um arquivo de texto contendo todos os nomes, um a cada linha. O nome do arquivo deve ser nomes_aleatorios.txt
>
>Passo 6: Abrir o arquivo e verificar seu conteúdo (editor de texto)

Acesse o arquivo compactado gerado pelo código: [arquivo](/sprint8/tarefa3/nomes_aleatorios.rar)

<br>

<a id="tarefa4"></a>
## 🧮 Tarefa 4 - Exercícios - Apache Spark

>Neste laboratório usaremos um arquivo CSV para criar um Dataframe e testar comandos SQL. Iremos utilizar o arquivo nomes_aleatorios.txt gerado na tarefa anterior. Esse arquivo tem aproximadamente 10 milhões de nomes distintos e apresenta os nomes mais populares registrados em cada ano.

>1.Inicialmente, precisamos copiar o arquivo nomes_aleatorios.txt para nosso diretório de trabalho.Após, em nosso script Python, devemos importar as bibliotecas necessárias:
>``` Python
>from pyspark.sql import SparkSession
>from pyspark import SparkContext, SQLContext
>```
>Aplicando as bibliotecas do Spark, podemos definir a Spark Session e sobre ela definir o Context para habilitar o módulo SQL
>```Python
>spark = SparkSession \
>                .builder \
>                .master("local[*]")\
>                .appName("Exercicio Intro") \
>                .getOrCreate()
>```

>2.Nesta etapa, adicione código para ler o arquivo nomes_aleatorios.txt através do comando spark.read.csv. Carregue-o para dentro de um dataframe chamado df_nomes e, por fim, liste algumas linhas através do método show. Exemplo: ```df_nomes.show(5)```

>3.Ao dataframe (df_nomes), adicione nova coluna chamada Escolaridade e atribua para cada linha um dos três valores de forma aleatória: Fundamental, Medio ou Superior.
>
>Para esta etapa, evite usar funções de iteração, como por exemplo: for, while, entre outras. Dê preferência aos métodos oferecidos para próprio Spark.

>4.Ao dataframe (df_nomes), adicione nova coluna chamada Pais e atribua para cada linha o nome de um dos 13 países da América do Sul, de forma aleatória.
>
>Para esta etapa, evite usar funções de iteração, como por exemplo: for, while, entre outras. Dê preferência aos métodos oferecidos para próprio Spark.

>5.Ao dataframe (df_nomes), adicione nova coluna chamada AnoNascimento e atribua para cada linha um valor de ano entre 1945 e 2010, de forma aleatória. 
>
>Para esta etapa, evite usar funções de iteração, como por exemplo: for, while, entre outras. Dê preferência aos métodos oferecidos para próprio Spark.

>6.Usando o método select do dataframe (df_nomes), selecione as pessoas que nasceram neste século. Armazene o resultado em outro dataframe chamado df_select e mostre 10 nomes deste.

>7.Usando Spark SQL repita o processo da Pergunta 6. Lembre-se que, para trabalharmos com SparkSQL, precisamos registrar uma tabela temporária e depois executar o comando SQL. Abaixo um exemplo de como executar comandos SQL com SparkSQL:
>``` Python
>df_nomes.createOrReplaceTempView ("pessoas")
>spark.sql("select * from pessoas").show()
>```

>8.Usando o método select do Dataframe df_nomes, Conte o número de pessoas que são da geração Millennials (nascidos entre 1980 e 1994) no Dataset

>9.Repita o processo da Pergunta 8 utilizando Spark SQL

>10.Usando Spark SQL, obtenha a quantidade de pessoas de cada país para uma das gerações abaixo. Armazene o resultado em um novo dataframe e depois mostre todas as linhas em ordem crescente de Pais, Geração e Quantidade
>- Baby Boomers – nascidos entre 1944 e 1964;
>- Geração X – nascidos entre 1965 e 1979;4
>- Millennials (Geração Y) – nascidos entre 1980 e 1994;
>- Geração Z – nascidos entre 1995 e 2015.

Fiz o exercício em um notebook Jupyter com Spark, acesse os códigos e os resultados pedidos: [notebook](/sprint8/tarefa4/spark.ipynb)