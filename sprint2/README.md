<h1 align="center"> Sprint 2</h1>

<p align="center">
 <a href="#exercicio-b">Exercícios SQL Biblioteca</a> •
 <a href="#exercicio-l">Exercícios SQL Loja</a> •
 <a href="#exercicio-ex">Exercícios SQL Exportação</a>
</p>

<br>

<a id="exercicio-b"></a>
## 📚 Exercícios SQL Biblioteca

<br>

### Complementos
- [Banco de dados para execução das querys](/sprint2/biblioteca.sqlite)
- Diagrama entidade relacionamento representando o banco de dados "Bibliioteca":
![biblioteca.sqlite](/sprint2/imagens-sprint2/DER%20-%20Biblioteca.png)

---

### Exercício 1
Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.  Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma
``` SQL
SELECT * --- As colunas pedidas são iguais as originais da tabela
FROM livro
WHERE publicacao  > '2014-12-31'
ORDER BY cod ASC
```
Saída da query:
![saída exercício 1](https://github.com/sTaissa/Compass-Uol/blob/main/sprint2/imagens-sprint2/e1.PNG)
![saída exercício 1](https://github.com/sTaissa/Compass-Uol/blob/main/sprint2/imagens-sprint2/e1.1.PNG)

### Exercício 2
Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  Atenção às colunas esperadas no resultado final:  titulo, valor.
``` SQL
SELECT titulo, valor
FROM livro
ORDER BY valor DESC --- Ordena do mais caro ao mais barato
LIMIT 10 --- Limita aos 10 mais caros
```
Saída da query: 

![saída exercício 2](https://github.com/sTaissa/Compass-Uol/blob/main/sprint2/imagens-sprint2/e2.PNG)

### Exercício 3
Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.
``` SQL
SELECT COUNT(*) as quantidade, edi.nome, en.estado, en.cidade
FROM livro AS li
--- Faz a ligação com a tabela editora e endereço para pegar os dados de cidade e estado das editoras
LEFT JOIN editora AS edi
	ON li.editora  = edi.codeditora 
LEFT JOIN endereco en 
	ON edi.endereco = en.codendereco 
GROUP BY edi.nome, en.estado, en.cidade
ORDER BY quantidade DESC
LIMIT 5
```
Saída da query: 

![saída exercício 3](https://github.com/sTaissa/Compass-Uol/blob/main/sprint2/imagens-sprint2/e3.PNG)

### Exercício 4
Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).
``` SQL
SELECT au.nome, au.codautor, au.nascimento, COUNT(li.cod) AS quantidade --- Conta a quantidade de livros da tabela livros relacionado a cada autor da tabela autor
FROM autor AS au
LEFT JOIN livro AS li
	ON li.autor = au.codautor 
GROUP BY au.nome, au.codautor, au.nascimento 
ORDER BY au.nome ASC
```
Saída da query: 

![saída exercício 4](https://github.com/sTaissa/Compass-Uol/blob/main/sprint2/imagens-sprint2/e4.PNG)
![saída exercício 4](https://github.com/sTaissa/Compass-Uol/blob/main/sprint2/imagens-sprint2/e4.1.PNG)
![saída exercício 4](https://github.com/sTaissa/Compass-Uol/blob/main/sprint2/imagens-sprint2/e4.2.PNG)
![saída exercício 4](https://github.com/sTaissa/Compass-Uol/blob/main/sprint2/imagens-sprint2/e4.3.PNG)

### Exercício 5
Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente.
``` SQL
SELECT au.nome
FROM autor AS au
--- Vários joins para linkar todas as tabelas que precisa para exibir os dados certos
LEFT JOIN livro AS li
	ON au.codautor = li.autor 
LEFT JOIN editora AS edi
	ON li.editora = edi.codeditora 
LEFT JOIN endereco AS en
	ON edi.endereco = en.codendereco 
WHERE en.estado NOT IN ("PARANÁ", "SANTA CATARINA", "RIO GRANDE DO SUL") --- Pega somente os dados das editoras que não ficam na região sul
ORDER BY au.nome ASC
```
Saída da query: 

![saída exercício 5](https://github.com/sTaissa/Compass-Uol/blob/main/sprint2/imagens-sprint2/e5.PNG)
![saída exercício 5](https://github.com/sTaissa/Compass-Uol/blob/main/sprint2/imagens-sprint2/e5.1.PNG)

### Exercício 6
Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.
``` SQL
SELECT au.codautor, au.nome, COUNT(*) AS quantidade_publicacoes --- Conta todos os livros por autor
FROM livro AS li
LEFT JOIN autor AS au 
	ON li.autor = au.codautor 
GROUP BY au.codautor, au.nome
ORDER BY quantidade_publicacoes DESC --- Lista do mais caro ao mais barato
LIMIT 1 --- Limita ao primeiro mais caro
```
Saída da query: 

![saída exercício 6](https://github.com/sTaissa/Compass-Uol/blob/main/sprint2/imagens-sprint2/e6.PNG)

### Exercício 7
Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.
``` SQL
SELECT nome
FROM autor AS au
LEFT JOIN livro AS li 
	ON au.codautor = li.autor
WHERE li.autor IS NULL --- Mostra apenas os autores que não tem correspondentes na tabela livros
ORDER BY autor ASC
```
Saída da query: 

![saída exercício 7](https://github.com/sTaissa/Compass-Uol/blob/main/sprint2/imagens-sprint2/e7.PNG)

<br>

<a id="exercicio-l"></a>
## 🏷️ Exercícios SQL Loja

<br>

### Complementos
- [Banco de dados para execução das querys](/sprint2/loja.sqlite)
- Diagrama entidade relacionamento representando o banco de dados "Loja":
![loja.sqlite](/sprint2/imagens-sprint2/DER_Loja.png)

---

### Exercício 8
Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.
``` SQL
SELECT ven.cdvdd, vdd.nmvdd
FROM tbvendas AS ven
LEFT JOIN tbvendedor AS vdd
	ON ven.cdvdd = vdd.cdvdd 
WHERE status = 'Concluído' -- Seleciona apenas as vendas concluídas para a contagem
GROUP BY ven.cdvdd, vdd.nmvdd -- Agrupa por vendedor
ORDER BY count(ven.cdven) DESC -- Ordena pena contagem mais alta
LIMIT 1 -- Limita ao primeiro vendedor com mais vendas
``` 
Saída da query: 

![saída exercício 8](/sprint2/imagens-sprint2/e8.PNG)

### Exercício 9
Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.
``` SQL
SELECT cdpro, nmpro
FROM tbvendas 
WHERE status = 'Concluído' --Seleciona apenas os produtos com status concluído para a contagem
	AND dtven BETWEEN '2014-02-03' AND '2018-02-02' --Seleciona apenas os produtos vendidos entre as datas especificadas
GROUP BY nmpro --Agrupa pelo nome do produto
ORDER BY count(cdpro) DESC --Realiza a contagem do produto e ordena pela mais alta
LIMIT 1 --Limita a contagem 1 contagem mais alta
``` 
Saída da query: 

![saída exercício 9](/sprint2/imagens-sprint2/e9.PNG)

### Exercício 10
A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.

As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.
``` SQL
WITH valor_total_vendas AS ( --Calcula o toal de vendido por cada vendedor (valor unitário * quantidade)
	SELECT cdvdd, SUM(qtd*vrunt) AS valor_total_vendas
	FROM tbvendas 
	WHERE status = 'Concluído' --Somente vendas concluídas
	GROUP BY cdvdd --Agrupa por vendedor
	ORDER BY valor_total_vendas DESC
)

SELECT 
	vdd.nmvdd AS vendedor, 
	vtv.valor_total_vendas, 
	ROUND(vtv.valor_total_vendas*vdd.perccomissao/100, 2) AS comissao --Calcula a comissão (valor de vendas * percentual) e arredonda pra 2 casas decimais
FROM tbvendedor AS vdd
LEFT JOIN valor_total_vendas AS vtv
	ON vdd.cdvdd = vtv.cdvdd
GROUP BY vdd.nmvdd --Agrupa por vendedor
ORDER BY comissao DESC
``` 
Saída da query: 

![saída exercício 10](/sprint2/imagens-sprint2/e10.PNG)

### Exercício 11
Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.
``` SQL
SELECT 
	cdcli, 
	nmcli, 
	SUM(qtd*vrunt) AS gasto --Soma o total vendido para cada cliente (cada venda é dada por quantidade * valor unitário)
FROM tbvendas 
GROUP BY cdcli, nmcli --Agrupa pelo cliente
ORDER BY gasto DESC --Ordena pelo maior gasto
LIMIT 1
``` 
Saída da query: 

![saída exercício 11](/sprint2/imagens-sprint2/e11.PNG)

### Exercício 12
Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.

Observação: Apenas vendas com status concluído.
``` SQL
WITH valor_total_vendas AS ( 
	--Calcula o total de vendas por cada vendedor (valor unitário * quantidade)
	SELECT cdvdd, SUM(qtd*vrunt) AS valor_total_vendas
	FROM tbvendas 
	WHERE status = 'Concluído' --Somente vendas concluídas
	GROUP BY cdvdd --Agrupa por vendedor
	ORDER BY valor_total_vendas ASC
	LIMIT 1 --Limita ao vendedor com menos vendas
)

--Seleciona os dependentes do vendedor com menos vendas
SELECT dep.cddep, dep.nmdep, dep.dtnasc, vtv.valor_total_vendas
FROM tbdependente AS dep
INNER JOIN valor_total_vendas AS vtv
	ON dep.cdvdd  = vtv.cdvdd
GROUP BY dep.cddep, dep.nmdep, dep.dtnasc  --Agrupa por dependente
``` 
Saída da query: 

![saída exercício 12](/sprint2/imagens-sprint2/e12.PNG)

### Exercício 13
 Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas). As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.
``` SQL
SELECT 
    cdpro, 
    nmcanalvendas, 
    nmpro, SUM(qtd) AS quantidade_vendas --Soma todas as unidades vendidas de cada produto
FROM tbvendas
WHERE status = 'Concluído' --Apenas vendas concluídas
GROUP BY cdpro, nmcanalvendas, nmpro
ORDER BY quantidade_vendas ASC
LIMIT 10 --Limita aos 10 produtos menos vendidos
``` 
Saída da query: 

![saída exercício 13](/sprint2/imagens-sprint2/e13.PNG)

### Exercício 14
Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

Observação: Apenas vendas com status concluído.
``` SQL
SELECT 
	estado, 
	ROUND(AVG(qtd*vrunt), 2) AS gastomedio --Faz a média do valor de cada venda e arredonda
FROM tbvendas 
WHERE status = 'Concluído' --Apenas vendas concluídas
GROUP BY estado --Agrupa por estado
ORDER BY gastomedio DESC --Ordena pelo maior gasto
``` 
Saída da query: 

![saída exercício 14](/sprint2/imagens-sprint2/e14.PNG)

### Exercício 15
Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.
``` SQL
SELECT cdven 
FROM tbvendas
WHERE deletado <> 0 --Seleciona as vendas onde o campo "deletado" é true (1)
ORDER BY cdven ASC
``` 
Saída da query: 

![saída exercício 15](/sprint2/imagens-sprint2/e15.PNG)

### Exercício 16
Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).
Obs: Somente vendas concluídas.
``` SQL
SELECT 
	estado,
	nmpro,
	ROUND(AVG(qtd), 4) AS quantidade_media --Calcula a quantidade média vendida de cada produto e arredonda para até 4 casas decimais
FROM tbvendas
WHERE status = 'Concluído' --Seleciona só vendas concluídas 
GROUP BY estado, nmpro --Agrupa por estado e produto
ORDER BY estado, nmpro --Ordena pelo estado e depois pelo produto
``` 
Saída da query: 

![saída exercício 16](/sprint2/imagens-sprint2/e16.PNG)

<br>

<a id="exercicio-ex"></a>
## 📚 Exercícios SQL Exportação

<br>

### Exercício 1

[Link](/sprint2/exercicios/10_livros_mais_caros.csv) para o arquivo CSV exportado da query para obter os 10 livros mais caros