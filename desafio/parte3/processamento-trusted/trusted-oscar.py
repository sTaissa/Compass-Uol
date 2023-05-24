"""
O código foi feito para rodar no AWS Glue, por isso, boa parte dele é gerado automaticamente pela ferramenta
"""

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#caminhos de origem e destino dos dados como parametros internos do job (configurados no Glue)
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

#cria um dataframe a partir do csv
df = spark.read.format("csv").option("sep","|").option("header", "true").option("inferSchema", "true").load(source_file)

#junta dados para ter apenas um arquivo parquet de saída
df_coalesce = df.coalesce(1)

#salva como parquet no s3
df_coalesce.write.parquet(target_path)

job.commit()