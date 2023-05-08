"""
Lembrando que o código foi feito para rodar no AWS Lambda na minha conta, onde foram configuradas 
bibliotecas, políticas de acesso e as credenciais do boto client não são necessárias.
"""

import json
import requests
import pandas as pd
import boto3
import apikey

def lambda_handler(event, context):
    #variáveis a serem usadas ao longo do código
    S3_CLIENT = boto3.client('s3')
    BUCKET = 'datalake-taissa'
    #localmente a chave está em um arquivo python, na AWS Lambda a chave vai no código já que apenas eu tenho acesso
    API_KEY = apikey.api_key
        
    #lê o csv com filmes do imdb armazenado no s3
    objeto = S3_CLIENT.get_object(Bucket=BUCKET, Key='Raw/Local/CSV/Movies/2023/04/24/movies.csv')
    filmes_imdb = pd.read_csv(objeto['Body'], sep='|')
    
    #retira os filmes duplicados com base em seus ids
    filmes_imdb = filmes_imdb.drop_duplicates(subset=['id'])
    
    #filtra apenas os filmes de animação do século 21 do csv
    filmes_imdb['anoLancamento'] = filmes_imdb['anoLancamento'].replace('\\N', '0')
    imdb_filtro = filmes_imdb[(filmes_imdb.genero.str.contains("Animation", regex=False)) & (filmes_imdb.anoLancamento.astype(int) >= 2000)]
    
    #passa por cada filme filtrado do csv, pegando o id e usando pra descobrir o id correspondente no tmdb
    for filme in imdb_filtro.values:
        id_imdb = filme[0]
    
        #acha o filme no tmdb com base no id do imdb 
        url = f"https://api.themoviedb.org/3/find/{id_imdb}?api_key={API_KEY}&language=pt-BR&external_source=imdb_id"
        response = requests.get(url)
        data = response.json()
    
        #no caso de um filme do csv do imdb não ter uma correspondencia no tmdb ele vai para o próximo filme
        try:
            #faz uma segunda requisição para pegar mais detalhes sobre o filme
            id_tmdb = data['movie_results'][0]['id']
            url = f"https://api.themoviedb.org/3/movie/{id_tmdb}?api_key={API_KEY}&language=pt-BR"
            response = requests.get(url)
            tmdb = response.json()
            
            #usa o nome do filme como nome do arquivo, substituindo espaços por - e / por \\, pois / cria uma pasta no s3
            file_name = f"{tmdb['title'].replace(' ', '-')}.json"
            file_name = file_name.replace('/', '\\')
            file_path = f'Raw/TMDB/JSON/2023/05/05/{file_name}'
            #armazena o resultado da requisição como json no s3 no caminho especificado
            S3_CLIENT.put_object(Body=json.dumps(tmdb, indent = 4), Bucket=BUCKET, Key=file_path)
        except:
            continue
        
    return {'statusCode': 200}