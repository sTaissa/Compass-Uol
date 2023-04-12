<h1 align="center"> Sprint 6</h1>

<p align="center">
 <a href="#sobre">Sobre</a> •
 <a href="#anotacoes">Anotações</a> •
 <a href="#labs">Laboratórios</a>
</p>

<br> 

<a id="sobre"></a>
## 📎 Sobre

### Mentor

[Aime Pereira](https://github.com/aimeepereira)

### Cursos e certificados

- [AWS Skill Builder - Data Analytics Fundamentals (Portuguese)](/certificados/sprint6_AWS-DataAnalytics.PNG)
- [AWS Partner: Data Analytics on AWS (Business) (Portuguese)](/certificados/sprint6_AWS-DataAnalytics-Business.PNG)
- [AWS Skill Builder - Introduction to Amazon Kinesis Streams](/certificados/sprint6_AWS-KinesisStreams.PNG)
- [AWS Skill Builder - Introduction to Amazon Kinesis Analytics](/certificados/sprint6_AWS-KinesisAnalytics.PNG)
- [AWS Skill Builder - Introduction to Amazon Elastic MapReduce (EMR) (Portuguese)](/certificados/sprint6_AWS-EMR.PNG)
- [AWS Skill Builder - Introduction to Amazon Athena (Portuguese)](/certificados/sprint6_AWS-Athena.PNG)
- [AWS Skill Builder - Introduction to Amazon Quicksight (Portuguese)](/certificados/sprint6_AWS-QuickSight.PNG)
- [AWS Skill Builder - Introduction to AWS IoT Analytics](/certificados/sprint6_AWS-IoT-Analytics.PNG)
- [AWS Skill Builder - Getting Started with Amazon Redshift](/certificados/sprint6_AWS-Redshift.PNG)
- [AWS Skill Builder - Deep Dive into Concepts and Tools for Analyzing Streaming Data (Portuguese)](/certificados/sprint6_AWS-Analysing-Streaming-Data.PNG)
- [AWS Skill Builder - Best Practices for Data Warehousing with Amazon Redshift (Portuguese)](/certificados/sprint6_AWS-DataWarehousing-with-Redshift.PNG)
- [AWS Skill Builder - Serverless Analytics (Portuguese)](/certificados/sprint6_AWS-Serverless-Analytics.PNG)
- [AWS Skill Builder - Why Analytics for Games (Portuguese)](/certificados/sprint6_AWS-AnalyticsGame.PNG)

<br>

<a id="anotacoes"></a>
## 📚 Anotações

[Anotações sobre AWS](https://lowly-pear-52e.notion.site/AWS-a43ecbd43e974b9087488e1e3b149f2b)

<br>

<a id="labs"></a>
## 👩‍💻  Laboratórios


### Lab AWS S3
>Explorar as capacidades do serviço AWS S3.  No passo a passo, você será guiado pelas configurações necessárias para que um bucket do Amazon S3 funcione como hospedagem de conteúdo estático.

#### Arquivos a colocar no bucket:
- [index.html](/sprint6/labs/arquivos/index.html)
- [dados/nomes.csv](/sprint6/labs/arquivos/dados/nomes.csv)
- [404.html](/sprint6/labs/arquivos/404.html)

Bucket com os arquivos pedidos e o acesso e políticas públicas:

![bucket publico](/sprint6/labs/lab1%20bucket.PNG)

Site rodando hospedado estaticamente no S3 criado:

![site lab1](/sprint6/labs/lab1%20site.PNG)

### Lab AWS Athena
>Após realizar o laboratório anterior, crie uma consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje usando o arquivo nomes.csv baixado anteriormente.

Query rodando no Athena após configurar tudo:
``` SQL
WITH decadas AS (
    SELECT
        nome, 
        CONCAT(SUBSTR(CAST(ano AS VARCHAR), 1, 3), '0') AS decada, --Substitui o último dígito do ano por 0, para ficar por décadas
        RANK() OVER(PARTITION BY CONCAT(SUBSTR(CAST(ano AS VARCHAR), 1, 3), '0') ORDER BY SUM(total) DESC, nome ASC) AS ROW --Numera as linhas separado por década ordenado pela soma total (nome mais usado)
    FROM meubanco.tabela
    WHERE ano BETWEEN 1950 AND 2023
    GROUP BY nome, CONCAT(SUBSTR(CAST(ano AS VARCHAR), 1, 3), '0') --Agrupa por nome e década para retirar nomes repetidos
)

SELECT 
    nome, 
    decada 
FROM decadas 
WHERE ROW IN (1,2,3) 
ORDER BY decada --Seleciona apenas os 3 primeiros nomes mais usados de cada década
```

Resultado da query:

![query1](/sprint6/labs/lab2%20resultado1.PNG)
![query2](/sprint6/labs/lab2%20resultado2.PNG)

### Lab AWS Lambda
>Após realizar os laboratórios anteriores, execute uma função Lambda.

#### Arquivo gerado pelo Docker para criar a camada e baixar as dependências necessárias pra rodar a função:
- [minha-camada-pandas.zip](/sprint6/labs/arquivos/minha-camada-pandas.zip)

Após as configurações, o código da função:
``` Python
import json
import pandas
import boto3


def lambda_handler(event, context):
    s3_client = boto3.client('s3')

    bucket_name = 'bucket-taissa'
    s3_file_name = 'dados/nomes.csv'
    objeto = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
    df=pandas.read_csv(objeto['Body'], sep=',')
    rows = len(df.axes[0])

    return {
        'statusCode': 200,
        'body': f"Este arquivo tem {rows} linhas"
    }
```

Saída da função:

![saida função](/sprint6/labs/lab3%20saida.PNG)
