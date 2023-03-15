<h1 align="center"> Sprint 3</h1>

<p align="center">
 <a href="#sobre">Sobre</a> •
 <a href="#exercicios-p">Exercícios Python Funcional</a> •
 <a href="#exercicios-d">Exercícios Docker e Python</a>
</p>

<br> 

<a id="sobre"></a>
## 📎 Sobre

### Conteúdos

- Python funcional
- Docker
- Estatística descritiva

### Mentor

[Rodrigo Guimarães](https://github.com/rodrigo-sguimaraes)


<br>

<a id="exercicios-p"></a>
## 🐍 Exercícios Python Funcional

<br>

### Exercício 1
>Você está recebendo um [arquivo](/sprint4/exercicios-programacao-funcional/number.txt) contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
Você deverá aplicar as seguintes funções no exercício:
>- map
>- filter
>- sorted
>- sum

> Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
>- a lista dos 5 maiores números pares em ordem decrescente;
>- a soma destes valores.

``` Python
# extrai os dados do arquivo e joga numa lista de int
def extrai(caminho):
    with open(caminho) as file:
        num = file.read().split("\n")
        num = list(map(lambda x: int(x), num))
        file.close()

    def filtra():
        par = lambda x: x % 2 == 0

        # filtra(filter) somente os pares da lista, ordena(sorted) esse resultado em ordem decrescente(reverse=True) e pega somente os 5 primeiros valores([0:5])
        return list(sorted(filter(par, num), reverse=True))[0:5]
    
    return filtra()


lista = extrai("sprint4/exercicios-programacao-funcional/number.txt")

print(lista)
print(sum(lista))
```

### Exercício 2
>Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.
É obrigatório aplicar as seguintes funções:
>- len
>- filter
>- lambda

> Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.

``` Python
def conta_vogais(texto:str)-> int:
    vogais = lambda x: x in ['a', 'e', 'i', 'o', 'u']
    # filtra as vogais da string e retorna o tamanho da lista gerada pela filtragem 
    return len(list(filter(vogais, texto.lower())))
```

### Exercício 3
>A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 
Abaixo apresentando uma possível entrada para a função.
>``` Python
>lancamentos = [
>    (200,'D'),
>    (300,'C'),
>    (100,'C')
>] 
>```

> A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. Na lista anterior, por exemplo, teríamos como resultado final 200.

>Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:
>- reduce (módulo functools)
>- map

``` Python
from functools import reduce 

def calcula_saldo(lancamentos) -> float:
    # usa map para criar uma lista com os valores da tupla, positivos se era 'C' e negativo se 'D'
    lista = list(map(lambda x: -x[0] if x[1] == 'D' else x[0], lancamentos))
    # retorna a soma de todos os valores da lista gerada
    return reduce(lambda x, y: x+y, lista)
```

### Exercício 4  
>A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %), as quais devem ser aplicadas à lista de operadores nas respectivas posições. Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles.
Veja o exemplo:
>- Entrada:
>``` Python
> operadores = ['+','-','*','/','+']
> operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]
>```
>- Aplicar as operações aos pares de operandos
>``` Python
> [ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ] 
>```
>- Obter o maior dos valores
>``` Python
> 12 
>```
> <br>

>Na resolução da atividade você deverá aplicar as seguintes funções:
>- max
>- zip
>- map

``` Python
def calcular_valor_maximo(operadores,operandos):
    # função a ser executada no map
    # eval calcula a operação passada em string
    operacao = lambda x: eval(f"{x[1][0]} {x[0]} {x[1][1]}")

    # junta os operadores com operandos através do 'zip', e usa essa lista para fazer os calculos com map
    return max(list(map(operacao, list(zip(operadores, operandos)))))
```

### Exercício 5 
>Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do [arquivo](/sprint4/exercicios-programacao-funcional/estudantes.csv) corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.

>Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:
>- Nome do estudante
>- Três maiores notas, em ordem decrescente
>- Média das três maiores notas, com duas casas decimais de precisão

>O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir: <br>
Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>

>Exemplo: <br>
Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67 <br>
Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33

>Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:
>- round
>- map
>- sorted
``` Python
import csv

# extrai os dados do arquivo e joga numa lista(num)
def extrai(caminho):
    file = open(caminho, encoding="utf-8")
    num = csv.reader(file)

    # filtra e retorna os valores pedidos
    def filtra():
        # função a ser passada no map, recebe uma lista (nome e 5 notas de uma aluno) e retorna uma lista já filtrada com apenas o nome e as 3 maiores notas
        def func(x):
            # transforma as 5 notas em int
            notas = list(map(lambda x: int(x), x[1:6]))
            # ordena pela maior nota
            notas = sorted(notas, reverse=True)
            # cria lista com o nome do aluno eas 3 maiores notas
            lista = [x[0], notas[:3]]
            return lista

        # aplica a função a cada aluno da lista e oredena pelo nome do aluno
        lista = sorted(list(map(func, num)))

        # retorna o relatório textual para cada aluno
        # a média é a soma das 3 notas / pelo tamamnho da lista e arredondado pra 2 casas
        file.close()
        return list(map(lambda x: print(f"Nome: {x[0]} Notas: {x[1]} Média: {round(sum(x[1])/len(x[1]), 2)}"), lista))
    return filtra()

extrai("sprint4/exercicios-programacao-funcional/estudantes.csv")
```

<br>

<a id="exercicios-d"></a>
##  🐋 Exercícios Docker e Python

<br>

### Extração 1
>Construa uma imagem a partir de um arquivo de instruções (Dockerfile) que execute o código [carguru.py](/sprint4/exercicios-docker/exercicio1/carguru.py). Após, execute um container a partir da imagem criada.

>Registre aqui o conteúdo de seu arquivo Dockerfile e o comando utilizado para execução do container.

``` Yaml
FROM python:3 

WORKDIR /sprint4/exercicios-docker/exercicio1 

COPY . .

CMD ["python", "./carguru.py"]
```
Comando para criar a imagem:
[E1 build](/sprint4/imagens-sprint4/build_exercicio1.PNG)

Comando para criar e executar o container:
[E1 run](/sprint4/imagens-sprint4/run_exercicio1.PNG)

### Exercício 2
>É possível reutilizar containers? Em caso positivo, apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker? Não sendo possível reutilizar, justifique sua resposta.

Sim, é possível, o comando usado apra isso é o "docker start [container]", podendo usar flags também, consultar o "start --help"

Utilizando o container do exercício anterior como exemplo:
[E2 start](/sprint4/imagens-sprint4/start_exercicio2.PNG)

### Exercício 2
>Agora vamos exercitar a criação de um container que permita receber inputs durante sua execução. Seguem as instruções.

>Criar novo script Python que implementa o algoritmo a seguir:
>1. Receber uma string via input
>2. Gerar o hash  da string por meio do algoritmo SHA-1
>3. Imprimir o hash em tela, utilizando o método hexdigest
>4. Retornar ao passo 1

>Criar uma imagem Docker chamada mascarar-dados que execute o script Python criado anteriormente

>Iniciar um container a partir da imagem, enviando algumas palavras para mascaramento

>Registrar o conteúdo do script Python, arquivo Dockerfile e comando de inicialização do container neste espaço.

Script de python (mascarar.py):
``` Python
import hashlib

# usa hash sha1 para mascarar a palavra passado como parâmetro
def mascara(palavra):
    return hashlib.sha1(palavra.encode("utf-8")).hexdigest()

# exibe o resultado da função passada como parâmetro até que seja digitado "sair"
def repete(func):
    while True:
        str = input("Informe a expressão a ser mascarada ou 'sair': ")

        if str.lower() != "sair":
            print(func(str))
            print()
        else: 
            break

repete(mascara)
```

Dockerfile:
``` YAML
FROM python:3 

WORKDIR /sprint4/exercicios-docker/exercicio3

COPY . .

CMD ["python", "./mascarar.py"]
```

Comando para criar a imagem:
[E3 build](/sprint4/imagens-sprint4/build_exercicio3.PNG)

Comando para criar e rodar o container:
[E3 run](/sprint4/imagens-sprint4/run_exercicio3.PNG)