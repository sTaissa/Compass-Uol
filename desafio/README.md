<h1 align="center"> Desafio </h1>

<p align="center">
 <a href="#sobre">Sobre</a> •
 <a href="#parte1">Parte 1</a> •
 <a href="#parte2">Parte 2</a> •
 <a href="#parte3">Parte 3</a> •
 <a href="#parte4">Parte 4</a>
</p>

<br> 

<a id="sobre"></a>
## 📎 Sobre

Ao final do programa de bolsas precisamos entregar um desafio: ingerir dados em batch sobre filmes e séries em um data lake na AWS e disponibilizar esses dados para visualização.

<a id="parte1"></a>
## 📤 Parte 1 - ETL

> Ingestão Batch: a ingestão dos arquivos CSV em Bucket Amazon S3 RAW Zone. Nesta etapa do desafio deve ser construído um código Python que será executado dentro de um container Docker para carregar os dados locais dos arquivos para a nuvem. Nesse caso utilizaremos, principalmente, as lib [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) como parte do processo de ingestão via batch para geração de arquivo (CSV).

![parte 1](/desafio/imagens-readme/parte1.png)

<br>

>1. Implementar código Python:
>- ler os 2 arquivos ([filmes e series](/desafio/parte1-etl/Filmes%2Be%2BSeries.zip)) no formato CSV inteiros, ou seja, sem filtrar os dados
>- utilizar a lib boto3 para carregar os dados para a AWS
>- acessar a AWS e gravar no S3, no bucket definido com RAW Zone

> No momento da gravação dos dados deve-se considerar o padrão: <nome do bucket>\<camada de armazenamento>\<origem do dado>\<formato do dado>\<especificação do dado>\<data de processamento separada por ano\mes\dia>\<arquivo>
> 
> Por exemplo:
>-  S3:\\data-lake-do-fulano\Raw\Local\CSV\Movies\2022\05\02\movies.csv
>- S3:\\data-lake-do-fulano\Raw\Local\CSV\Series\2022\05\02\series.csv

``` Python
import logging
import boto3
from botocore.exceptions import ClientError
import os

# As chaves de acesso são acessadas por variáveis de ambiente (com docker pelo arquivo .env)
s3_client = boto3.client(
        's3', 
        aws_access_key_id=os.environ['AWS_ACCESS_KEY'], 
        aws_secret_access_key=os.environ['AWS_SECRET_KEY'], 
        aws_session_token=os.environ['AWS_SESSION_TOKEN'],
        region_name='us-east-1')

def upload_file(origem, bucket, destino):
    # tenta fazer o upload do arquivo no bucket, retorna True se der certo
    try:
        response = s3_client.upload_file(origem, bucket, destino)
    except ClientError as e:
        logging.error(e)
        return False
    return True

print(upload_file('dados/movies.csv', 'datalake-taissa', 'Raw/Local/CSV/Movies/2023/04/24/movies.csv'))
print(upload_file('dados/series.csv', 'datalake-taissa', 'Raw/Local/CSV/Series/2023/04/24/series.csv'))
```

<br>

>2. Criar container Docker com um volume para armazenar os arquivos CSV e executar processo Python implementado
>3. Executar localmente o container docker para realizar a carga dos dados ao S3

Dockerfile para criar a imagem do container:
``` YAML
FROM python:3

WORKDIR /app

COPY . .

RUN pip install boto3

CMD ["etl.py"]

ENTRYPOINT ["python3"]
```
Comandos docker para criar a imagem e o container com um volume para persistir os arquivos csv:
![comandos dockes](/desafio/imagens-readme/parte1-comandos.PNG)
Eu utilizei um arquivo .env com as chaves de acesso aws configuradas como variáveis de ambiente e passei esse arquivo para o docker com a tag "--env-file" para que o código pudesse usar esses valores como variáveis de ambiente. Dessa forma as credenciais não ficam diretamente no código e é prático pra atualizá-las.

Bucket com os arquivos upados:
![bucket](/desafio/imagens-readme/parte1-bucket.PNG)