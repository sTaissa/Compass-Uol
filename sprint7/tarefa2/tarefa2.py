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
