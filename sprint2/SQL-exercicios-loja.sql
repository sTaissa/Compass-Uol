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
FROM tbvendas AS ven
WHERE status = 'Concluído' --Apenas vendas concluídas
GROUP BY cdpro, nmcanalvendas, nmpro
ORDER BY quantidade_vendas ASC
LIMIT 10 --Limita aos 10 produtos menos vendidos

