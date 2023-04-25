<h1 align="center"> Sprint 7</h1>

<p align="center">
 <a href="#sobre">Sobre</a> •
 <a href="#tarefa1">Tarefa 1</a> •
 <a href="#tarefa2">Tarefa 2</a> •
 <a href="#desafio">Desafio parte 1</a>
</p>

<br> 

<a id="sobre"></a>
## 📎 Sobre

### Mentor

Diego Antonio Lusa

### Cursos
- [Learn By Example: Hadoop, MapReduce for Big Data problems](https://www.udemy.com/course/learn-by-example-hadoop-mapreduce/)
- [Formação Spark com Pyspark : o Curso Completo](https://www.udemy.com/course/spark-curso-completo/?utm_source=adwords-intl&utm_medium=udemyads&utm_campaign=LongTail_new_la.PT_cc.BR&utm_content=deal4584&utm_term=_._ag_118044111562_._kw__._ad_491671393399_._de_c_._dm__._pl__._ti_dsa-1131315795548_._li_9047798_._pd__._&gclid=CjwKCAjw9J2iBhBPEiwAErwpeZ-3bys18AOcblMFlQx3eJjdpBRz-8hp3mNwFIBs8nod1muxs1X40RoC96QQAvD_BwE)


### Anotações
- [Hadoop](https://lowly-pear-52e.notion.site/Hadoop-b19eb01123124df38a06e16ef57d68f7)
- [Spark e Pyspark](https://lowly-pear-52e.notion.site/Spark-e-PySpark-b238560dafbb45768d177de12359854a)

<br>

<a id="tarefa1"></a>
## 🐼 Tarefa 1 - Python com Pandas e NumPy

>Leia o arquivo [actors.csv](/sprint7/tarefa1/actors.csv) e codifique os cálculos solicitados sobre o conjunto de dados utilizando a biblioteca Pandas:

> 1. Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.
> 2. Apresente a média da coluna contendo o número de filmes.
> 3. Apresente o nome do ator/atriz com a maior média por filme.
> 4. Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

Eu fiz em um notebook Jupyter, com cada célula sendo um exercício e sua respectiva saída, acesse para conferir: [notebook](/sprint7/tarefa1/tarefa1.ipynb)

<br>

<a id="tarefa2"></a>
## 📝 Tarefa 2 - Apache Spark, Contador de Palavras

### Exercício 1
>Neste exercícios iremos construir um job Spark por meio de um container Docker

>Siga os passos a seguir para executar o Spark utilizando uma imagem Docker:
> 1. Instalar o Docker. [Link para dowload](https://docs.docker.com/desktop/install/windows-install)
> 2. Instalar o Visual Studio Code. [Link para downloas](https://code.visualstudio.com/Download)
> 3. Instalar as extensões  abaixo no Visual Studio Code:
> - Python [ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
> - [Dev - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
> 4. Criar no seu diretório de trabalho (uma pasta onde você terá o código-fonte) um arquivo chamado Dockerfile e inserir o seguinte conteúdo:
> ``` YAML
>FROM jupyter/all-spark-notebook
>```
> 5. No menu View do Visual Studio Code, clicar em Command Pallete (ou Ctrl + Shift + P) e executar o comando Dev Containers: Open Folder in Container...
> 6. Selecionar a opção From 'Dockerfile'
> 7. Clicar em Reopen in Container no pop-up que aparece no canto inferior direito do VS Code.

> Usando o Spark Shell, faça um programa que conte as palavras de um arquivo README.md (que você mesmo pode criar). Caso opte por um arquivo existente, podes utilizar o disponível neste endereço: https://github.com/apache/spark/blob/master/README.md

``` Python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('WordCount').getOrCreate()

#lê o arquivo
arquivo = spark._sc.textFile("./README-teste.md")

#filtra o arquivo para remover linhas em branco
arquivo_limpo = arquivo.filter(lambda x: len(x) > 0)

#usa a função flatMap om um lambda para dividir cada linha em palavras pelo espaço e juntar tudo em uma lista só
palavras = arquivo_limpo.flatMap(lambda linha: linha.lower().strip().split(" "))

#cria uma tupla com cada palavra e o número 1 para posterior contagem (função Map do MapReduce)
palavras = palavras.map(lambda palavra: (palavra, 1))

#usa a função reduceByKey para juntar as palavras iguais e somar a quantidade de 1 respectiva (função Reduce do MapReduce)
contagem = palavras.reduceByKey(lambda a, b: a + b)

#ordena a lista da palavra que mais aparece para a que menos aparece
ordenado = contagem.map(lambda x:(x[1],x[0])).sortByKey(False)

#realiza a ação spark e exibe os valores
for i in ordenado.collect():
    print(i)
```

Resultado no terminal Pyspark:

![resultado tarefa 2](/sprint7/imagens-readme/tarefa2-resultado.PNG)

<a id="desafio"></a>
## 📤 Desafio parte 1 - ETL

Temos um desafio final para entregar ao fim do programa, nessa sprint realizamos a primeira parte dele, acesse: [desafio](/desafio/)
