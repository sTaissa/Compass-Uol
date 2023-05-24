"""
O código foi feito para rodar no AWS Glue, por isso, boa parte dele é gerado automaticamente pela ferramenta
"""

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import expr, row_number
from pyspark.sql.window import Window

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_MOVIES', 'S3_INPUT_TMDB', 'S3_INPUT_OSCAR', 'S3_TARGET_FILME', 'S3_TARGET_AVALIACAO', 'S3_TARGET_FINANCEIRO'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#caminhos de origem e destino dos dados como parametros internos do job (configurados no Glue)
source_movies = args['S3_INPUT_MOVIES']
source_tmdb = args['S3_INPUT_TMDB']
source_oscar = args['S3_INPUT_OSCAR']
destino_filme = args['S3_TARGET_FILME']
destino_financeiro = args['S3_TARGET_FINANCEIRO']
destino_avaliacao = args['S3_TARGET_AVALIACAO']

#le os arquivos parquet salvos na trusted zone
csv = spark.read.parquet(source_movies)
json = spark.read.parquet(source_tmdb)
oscar = spark.read.parquet(source_oscar)

#filtra csv para pegar apenas dados de filmes de animações a partir dos anos 2000 e longa metragem (acima de 40 minutos)
csv = csv.filter(csv["genero"].contains("Animation") & (csv["anoLancamento"] >= 2000) & (csv["tempoMinutos"] >= 40))

#filtra pra só ter filmes feitos pela disney
json = json.filter(expr("exists(production_companies, g -> g.name like '%Disney%')"))

#cria a "tabela" financeiro de acordo com o modelo
financeiro = json.select(json["budget"].alias("orcamento"), json["revenue"].alias("receita"))
financeiro = financeiro.drop_duplicates()

#cria coluna com ids unicos
window = Window.orderBy("orcamento")
financeiro = financeiro.withColumn("id", row_number().over(window))

#cria a "tabela" avaliacao de acordo com o modelo
nota = json.join(csv, json["imdb_id"] == csv["id"], "inner").select(json["vote_average"].alias("notaTMDB"), json["vote_count"].alias("votosTMDB"), csv["notaMedia"].alias("notaIMDB"), csv["numeroVotos"].alias("votosIMDB"))

#cria coluna com ids unicos
window = Window.orderBy("notaTMDB")
nota = nota.withColumn("id", row_number().over(window))

#cria "tabela" filme de acordo com o modelo
filme = json.join(csv, json["imdb_id"] == csv["id"]).join(financeiro, (json["budget"] == financeiro["orcamento"]) & (json["revenue"] == financeiro["receita"])).join(nota, (json["vote_average"] == nota["notaTMDB"]) & (csv["notaMedia"] == nota["notaIMDB"]) & (json["vote_count"] == nota["votosTMDB"]) & (csv["numeroVotos"] == nota["votosIMDB"])).join(oscar, oscar["filme"] == json["title"], "left").select(json["title"].alias("titulo"), json["release_date"].alias("lancamento"), financeiro["id"].alias("id_financeiro"), nota["id"].alias("id_nota"), json["popularity"].alias("popularidade"), oscar["anoPremiacao"].alias("oscar"))

#cria coluna com ids unicos
window = Window.orderBy("titulo")
filme = filme.withColumn("id", row_number().over(window))

#salva em parquet
financeiro = financeiro.coalesce(1)
nota = nota.coalesce(1)
filme = filme.coalesce(1)

financeiro.write.format("parquet").mode("overwrite").option("path", destino_financeiro).saveAsTable("desafio.dim_financeiro")
nota.write.format("parquet").mode("overwrite").option("path", destino_avaliacao).saveAsTable("desafio.dim_avaliacao")
filme.write.format("parquet").mode("overwrite").option("path", destino_filme).saveAsTable("desafio.fato_filme")

job.commit()