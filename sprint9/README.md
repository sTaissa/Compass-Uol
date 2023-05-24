<h1 align="center"> Sprint 9</h1>

<p align="center">
 <a href="#sobre">Sobre</a> •
 <a href="#tarefa1">Tarefa 1</a> •
 <a href="#tarefa2">Tarefa 2</a> •
 <a href="#desafio">Desafio parte 3</a>
</p>

<br> 

<a id="sobre"></a>
## 📎 Sobre

### Mentor

Augusto Luiz da Costa Schnorr

<br>

<a id="tarefa1"></a>
## 📋 Tarefa 1 - Modelagem Relacional Normalização

>O desafio é normalizar a base de dados concessionária, ou seja, aplicar as formas normais, modelo para normalizar:
>
> ![concessionaria](/sprint9/imagens-readme/concessionaria.png)

>Observações:
>
>Para auxiliar na resolução, você poderá baixar o arquivo contendo o banco de dados [concessionaria.zip](/sprint9/tarefa1/concessionaria.zip) para seu computador, e, com auxílio de algum cliente SQL, executar as queries localmente. Lembre-se de descompactar o arquivo antes.

Arquivo .sql com a base de dados normalizada: [concessionaria-normalizado.sql](/sprint9/tarefa1/concessionaria-normalizado.sql)

Modelo gerado pelo DBeaver ao trabalhar na base de dados:
![modelagem-normalizada](/sprint9/imagens-readme/ERnormalizado.PNG)

Com base nas 3 formas normais, criei as tabelas para carro, cliente e vendedor, para não ter repetições (1FN), para que cada tabela tenha informações sobre apenas uma entidade (2FN) e para remover campos que não dependam da chave primária idLocacao (3FN).  Seguindo esse pensamento, também criei as tabelas, combustível, modelo e marca. Além disso, seguindo as formas de normalização também criei as tabelas cidade estado e país, visto que se relacionam entre si e são dados compartilhados entre vendedor e cliente.

<br>

<a id="tarefa2"></a>
## 📝 Tarefa 2 - Modelagem Dimensional - Criação de modelo

>O desafio é montar o Modelo Dimensional com base no [Modelo Relacional](/sprint9/tarefa1/concessionaria-normalizado.sql) (normalizado - feito por vocês) na seção anterior.

>Observações:
>
>Dica: Criar views para fatos e dimensões

Observação: criei tabelas e não views para poder usar chaves estrangeiras e gerar as relações na modelagem.

Arquivo .sql com a base de dados dimensional: [concessionaria-dimensional.sql](/sprint9/tarefa2/concessionaria-dimensional.sql)

Modelagem gerada pelo DBeaver: ![modelagem-dimensional](/sprint9/imagens-readme/ERdimensional.PNG)
<br>

<a id="desafio"></a>
## 📤 Desafio parte 3 - Tarefas 3, 4 e 5

Temos um desafio final para entregar ao fim do programa, nessa sprint realizamos a terceira parte dele, acesse: [desafio](/desafio/)

<br>

