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

Ao final do programa de bolsas precisamos entregar um desafio: ingerir dados em batch sobre filmes e séries para um data lake na AWS, realizar uma análise e disponibilizar esses dados para visualização, extraindo valor dos dados coletados.

### Tema
Cada squad recebeu um gênero de filmes/séries para trabalhar em cima, meus gêneros são animação e/ou comédia.

Com base nisso o tema da minha análise e desafio final é: **Os melhores e piores filmes da Disney lançados no século 21**

<a id="parte1"></a>
## 📤 Parte 1 - ETL

> Ingestão Batch: a ingestão dos arquivos CSV em Bucket Amazon S3 RAW Zone. Nesta etapa do desafio deve ser construído um código Python que será executado dentro de um container Docker para carregar os dados locais dos arquivos para a nuvem. Nesse caso utilizaremos, principalmente, as lib [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) como parte do processo de ingestão via batch para geração de arquivo (CSV).
>
>![parte 1](/desafio/imagens-readme/parte1.png)

<br>

>1.Implementar código Python:
>- ler os 2 arquivos ([filmes e series](/desafio/parte1-etl/Filmes%2Be%2BSeries.zip)) no formato CSV inteiros, ou seja, sem filtrar os dados
>- utilizar a lib boto3 para carregar os dados para a AWS
>- acessar a AWS e gravar no S3, no bucket definido com RAW Zone
>
> No momento da gravação dos dados deve-se considerar o padrão: <nome do bucket>\<camada de armazenamento>\<origem do dado>\<formato do dado>\<especificação do dado>\<data de processamento separada por ano\mes\dia>\<arquivo>
> 
> Por exemplo:
>-  S3:\\data-lake-do-fulano\Raw\Local\CSV\Movies\2022\05\02\movies.csv
>- S3:\\data-lake-do-fulano\Raw\Local\CSV\Series\2022\05\02\series.csv

Acesse o código que carrega os arquivos csv para o S3: [meu código](/desafio/parte1-etl/etl.py)


>2. Criar container Docker com um volume para armazenar os arquivos CSV e executar processo Python implementado
>3. Executar localmente o container docker para realizar a carga dos dados ao S3

Dockerfile para criar a imagem do container: [dockerfile](/desafio/parte1-etl/Dockerfile)

Comandos docker para criar a imagem e o container com um volume para persistir os arquivos csv:

![comandos dockes](/desafio/imagens-readme/parte1-comandos.PNG)

Eu utilizei um arquivo .env com as chaves de acesso aws configuradas como variáveis de ambiente e passei esse arquivo para o docker com a tag "--env-file" para que o código pudesse usar esses valores como variáveis de ambiente. Dessa forma as credenciais não ficam diretamente no código e é prático pra atualizá-las.

Bucket com os arquivos upados:

![bucket](/desafio/imagens-readme/parte1-bucket.PNG)

<a id="parte2"></a>
## 📤 Parte 2 - Ingestão de dados do Twitter e/ou TMBD

>Neste etapa do desafio, nos iremos capturar tweets em tempo real com Python por meio da lib tweepy e/ou dados existentes na API do TMDB via AWS Lambda. Os dados coletados devem ser persistidos em Amazon S3, camada de RAW Zone, mantendo o formato da origem (JSON) e, se possível, agrupando-os em arquivos com, no máximo, 100 tweets cada
>
>O objetivo desta etapa é enriquecer os dados dos Filmes e Series carregados na Etapa 1 com dados externos do Twitter e/ou do TMDB e/ou de outra API a sua escolha.
>
>Importante:
>
>- Os arquivos CSVs carregados na Etapa 1 não devem ser modificados.
>- Os novos dados devem ser complementares aos dados do CSV. Tem que existir informações novas sobre os dados do CSV.
>- Não é necessário realizar tratamento dos dados externos, o máximo que pode ser feito é o agrupamento de dados.
>- Cuidado para os arquivos JSON gerados não serem maior do que 10 MB.
>- Não agrupe JSON com estruturas diferentes.
>- Se você escolher por fazer o desafio por todos atores ou séries ou filmes de uma ou mais categorias, utilize o CSV carregado na Etapa 1 como fonte de entrada para localização dos IDs do IMDB para depois realizar a pesquisa no TMDB.
>- Se você escolher fazer sobre um filme ou uma trilogia específica, considere utilizar pelo menos 4 métodos de API diferentes para possibilitar uma análise de dados qualificada.
>- Considere desenvolver seu código localmente primeiro e com poucos dados para depois leva-lo para a AWS Lambda e aumentar a pesquisa de dados. APIs normalmente limitam requisições. Evite realizar muitas requisições em fase de desenvolvimento ou teste para evitarmos qualquer bloqueio na conta de vocês
>
>![imagem parte 2](/desafio/imagens-readme/parte2.png)

>Em sua conta AWS, no serviço AWS Lambda, realize as seguintes atividades:
>1.  Criar nova camada (layer) no AWS Lambda para as libs necessárias à ingestão de dados (por exemplo,  tweepy, se você utilizar o Tweeter)

Como não usei a API do Twitter, criei uma camada para poder usar Pandas no código AWS Lambda

>2. Implementar o código Python em AWS Lambda para consumo de dados do Twitter/TMDB:
>   - Se está utilizando Twitter, buscar os tweets de interesse para a análise (neste ponto você já deve ter definido qual análise planeja realizar com os dados) e agrupar os tweets em arquivo JSON com, no máximo, 100 registros cada
>   - Se está utilizando TMDB,  buscar pela API os dados que complementem a análise
>   - Utilizar a lib boto3 para gravar os dados no AWS S3
>
>No momento da gravação dos dados deve-se considerar o padrão de path: <nome do bucket>\<camada de armazenamento>\<origem do dado>\<formato do dado>\<especificação do dado>\<data de processamento separada por ano\mes\dia>\<arquivo>
>
> São exemplos de caminhos de arquivos válidos:
>- S3:\\data-lake-do-fulano\Raw\Twitter\JSON\2022\05\02\prt-uty-nfd.json
>- S3:\\data-lake-do-fulano\Raw\Twitter\JSON\2022\05\02\idf-uet-wqt.json

Acesse meu código que consome os dados da API TMDB para os filmes de animação do século 21, como um complemento das informações do csv: [código](/desafio/parte2-ingestao/tmdb-ingestao.py)

Dados já upados no S3 pelo código:

![bucket](/desafio/imagens-readme/parte2-bucket.PNG)
![bucket2](/desafio/imagens-readme/parte2-bucket1.PNG)

>3. Caso esteja utilizando o Twitter, execute a função Lambda periodicamente para alimentar seu conjunto de dados no S3.
>
>Informação adicional:
>Podemos utilizar os serviços  CloudWatch Event ou Amazon EventBridge para agendar extrações periódicas de dados no Twitter de forma automática.

### Observações:
Para ser possível acessar o serviço S3 dentro da função Lambda, foi preciso criar uma política de permissão para a função no AWS IAM, com o seguinte código:
``` JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::datalake-taissa/*"
        }
    ]
}
```
Além disso, foi preciso configurar uma política do bucket para permitir esse acesso também:
``` Json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::datalake-taissa/*"
        }
    ]
}
```