-- E8: Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas 
-- vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.
SELECT ven.cdvdd, vdd.nmvdd
FROM tbvendas AS ven
LEFT JOIN tbvendedor AS vdd
	ON ven.cdvdd = vdd.cdvdd 
WHERE status = 'Concluído' -- Seleciona apenas as vendas concluídas para a contagem
GROUP BY ven.cdvdd, vdd.nmvdd -- Agrupa por vendedor
ORDER BY count(ven.cdven) DESC -- Ordena pena contagem mais alta
LIMIT 1 -- Limita ao primeiro vendedor com mais vendas

