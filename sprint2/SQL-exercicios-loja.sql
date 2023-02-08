-- E8: Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas 
-- vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.
SELECT ven.cdvdd, vdd.nmvdd
FROM tbvendas AS ven
LEFT JOIN tbvendedor AS vdd
	ON ven.cdvdd = vdd.cdvdd 
WHERE status = 'Concluído' -- Seleciona apenas as vendas concluídas para a contagem
GROUP BY ven.cdvdd, vdd.nmvdd -- Agrupa por vendedor
ORDER BY count(ven.cdven) DESC -- Realiza a contagem e ordena pela mais alta
LIMIT 1 -- Limita ao primeiro vendedor com mais vendas


-- E9: Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, 
-- e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.
SELECT cdpro, nmpro
FROM tbvendas 
WHERE status = 'Concluído' --Seleciona apenas os produtos com status concluído para a contagem
	AND dtven BETWEEN '2014-02-03' AND '2018-02-02' --Seleciona apenas os produtos vendidos entre as datas especificadas
GROUP BY nmpro --Agrupa pelo nome do produto
ORDER BY count(cdpro) DESC --Realiza a contagem do produto e ordena pela mais alta
LIMIT 1 --Limita a contagem 1 contagem mais alta

