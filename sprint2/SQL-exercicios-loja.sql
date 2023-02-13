-- E8: Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas 
--vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.
SELECT ven.cdvdd, vdd.nmvdd
FROM tbvendas AS ven
LEFT JOIN tbvendedor AS vdd
	ON ven.cdvdd = vdd.cdvdd 
WHERE status = 'Concluído' -- Seleciona apenas as vendas concluídas para a contagem
GROUP BY ven.cdvdd, vdd.nmvdd -- Agrupa por vendedor
ORDER BY count(ven.cdven) DESC -- Realiza a contagem e ordena pela mais alta
LIMIT 1 -- Limita ao primeiro vendedor com mais vendas


-- E9: Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, 
--e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.
SELECT cdpro, nmpro
FROM tbvendas 
WHERE status = 'Concluído' --Seleciona apenas os produtos com status concluído para a contagem
	AND dtven BETWEEN '2014-02-03' AND '2018-02-02' --Seleciona apenas os produtos vendidos entre as datas especificadas
GROUP BY nmpro --Agrupa pelo nome do produto
ORDER BY count(cdpro) DESC --Realiza a contagem do produto e ordena pela mais alta
LIMIT 1 --Limita a contagem 1 contagem mais alta


-- E10: --A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele 
--realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

--Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base 
--de dados com status concluído.

--As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado 
--em ordem decrescente arredondado na segunda casa decimal.
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
	ROUND(vtv.valor_total_vendas*(vdd.perccomissao/100), 2) AS comissao --Calcula a comissão (valor de vendas * percentual) e arredonda pra 2 casas decimais
FROM tbvendedor AS vdd
LEFT JOIN valor_total_vendas AS vtv
	ON vdd.cdvdd = vtv.cdvdd
GROUP BY vdd.nmvdd --Agrupa por vendedor
ORDER BY comissao DESC


-- E11: Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado 
--devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.
SELECT 
	cdcli, 
	nmcli, 
	SUM(qtd*vrunt) AS gasto --Soma o total vendido para cada cliente (cada venda é dada por quantidade * valor unitário)
FROM tbvendas 
GROUP BY cdcli, nmcli --Agrupa pelo cliente
ORDER BY gasto DESC --Ordena pelo maior gasto
LIMIT 1


-- E12: Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total 
--bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
-- Observação: Apenas vendas com status concluído.
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


-- E13: Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas 
--concluídas). As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.
SELECT 
    cdpro, 
    nmcanalvendas, 
    nmpro, SUM(qtd) AS quantidade_vendas --Soma todas as unidades vendidas de cada produto
FROM tbvendas
WHERE status = 'Concluído' --Apenas vendas concluídas
GROUP BY cdpro, nmcanalvendas, nmpro
ORDER BY quantidade_vendas ASC
LIMIT 10 --Limita aos 10 produtos menos vendidos


-- E14: Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e 
--gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.
-- Observação: Apenas vendas com status concluído.
SELECT 
	estado, 
	ROUND(AVG(qtd*vrunt), 2) AS gastomedio --Faz a média do valor de cada venda e arredonda
FROM tbvendas 
WHERE status = 'Concluído' --Apenas vendas concluídas
GROUP BY estado --Agrupa por estado
ORDER BY gastomedio DESC --Ordena pelo maior gasto


-- E15: Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.
SELECT cdven 
FROM tbvendas
WHERE deletado <> 0 --Seleciona as vendas onde o campo "deletado" é true (1)
ORDER BY cdven ASC


-- E16: Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes 
--no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta 
--casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).
-- Obs: Somente vendas concluídas.
SELECT 
	estado,
	nmpro,
	ROUND(AVG(qtd), 4) AS quantidade_media --Calcula a quantidade média vendida de cada produto e arredonda para até 4 casas decimais
FROM tbvendas
WHERE status = 'Concluído' --Seleciona só vendas concluídas 
GROUP BY estado, nmpro --Agrupa por estado e produto
ORDER BY estado, nmpro --Ordena pelo estado e depois pelo produto