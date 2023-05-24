"""
O código foi feito para rodar no AWS Glue, por isso, boa parte dele é gerado automaticamente pela ferramenta
"""

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import when
from pyspark.sql.types import DateType

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH','S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#caminhos de origem e destino dos dados como parametros internos do job (configurados no Glue)
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

#le os arquivos json armazenados no s3
df = spark.read.option("multiline","true").json(source_file)

#transforma colunas com string vazias "" em campos nulos
columns = df.columns

for col in columns:
    data_type = dict(df.dtypes)[col]
    if data_type == "string":
        df = df.withColumn(col, when(df[col] == "", None).otherwise(df[col]))

#transforma a coluna 'release_date' para o tipo data
df = df.withColumn("release_date", df["release_date"].cast(DateType()))

#remove linhas vazias
df = df.filter(df['id'].isNotNull())

#particiona em 1 arquivo só, já que é pequeno
df = df.coalesce(1)

#salva o arquivo em parquet
df.write.parquet(target_path)

job.commit()