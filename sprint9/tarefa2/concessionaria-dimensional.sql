/*Apesar da recomendação ser usar views, para gerar oa relações no diagrama o monitor me aoconelhou a usar tabelas nas dimensões*/

-- Dimensão cliente
CREATE TABLE dim_cliente AS 
SELECT c.idCliente, c.nomeCliente, ci.nomeCidade, e.nomeEstado, p.nomePais
FROM tb_cliente AS c
INNER JOIN tb_cidade AS ci 
	ON c.idCidade = ci.idCidade 
INNER JOIN tb_estado AS e 
	ON ci.idEstado = e.idEstado 
INNER JOIN tb_pais AS p
	ON e.idPais = p.idPais;
	
-- Dimensão vendedor
CREATE TABLE dim_vendedor AS
SELECT v.idVendedor, v.nomeVendedor, v.sexoVendedor, e.nomeEstado
FROM tb_vendedor AS v
INNER JOIN tb_estado AS e
	ON v.idEstado = e.idEstado;

-- Dimensão carro
CREATE TABLE dim_carro AS
SELECT c.idCarro, c.classiCarro, m.nomeMarca, mo.nomeModelo, c.anoCarro, co.tipoCombustivel
FROM tb_carro AS c
INNER JOIN tb_modeloCarro AS mo 
	ON c.idModelo = mo.idModelo 
INNER JOIN tb_marcaCarro AS m 
	ON mo.idMarca = m.idMarca 
INNER JOIN tb_combustivel AS co 
	ON c.idCombustivel = co.idCombustivel;

-- Dimensão data de locacao
CREATE TABLE dim_dtLocacao AS
SELECT 
	dataLocacao, 
	CAST(strftime('%Y', dataLocacao) AS INT) AS ano,
	CAST(strftime('%m', dataLocacao) AS VARCHAR(10)) AS mes,
	CAST(strftime('%w', dataLocacao) AS SMALLINT) AS semana,
	CAST(strftime('%d', dataLocacao) AS SMALLINT) AS dia,
	horaLocacao AS hora
FROM tb_locacao;

-- Dimensão data de entrega
CREATE TABLE dim_dtEntrega AS
SELECT 
	dataEntrega, 
	CAST(strftime('%Y', dataEntrega) AS INT) AS ano,
	CAST(strftime('%m', dataEntrega) AS VARCHAR(10)) AS mes,
	CAST(strftime('%w', dataEntrega) AS SMALLINT) AS semana,
	CAST(strftime('%d', dataEntrega) AS SMALLINT) AS dia,
	horaEntrega AS hora
FROM tb_locacao;

-- Fato locação
CREATE TABLE fato_locacao (
idLocacao INT, 
idCliente INT, 
idCarro INT, 
kmCarro INT, 
dataLocacao DATETIME, 
dataEntrega DATETIME, 
vlrDiaria DECIMAL(18,2), 
idVendedor INT,
CONSTRAINT idCliente FOREIGN KEY (idCliente) REFERENCES dim_cliente(idCliente),
CONSTRAINT idCarro FOREIGN KEY (idCarro) REFERENCES dim_carro(idCarro),
CONSTRAINT dataLocacao FOREIGN KEY (dataLocacao) REFERENCES dim_dtlocacao(dataLocacao),
CONSTRAINT dataEntrega FOREIGN KEY (dataEntrega) REFERENCES dim_dtEntrega(dataEntrega),
CONSTRAINT idVendedor FOREIGN KEY (idVendedor) REFERENCES dim_vendedor(idVendedor));

INSERT INTO fato_locacao (idLocacao, idCliente, idCarro, kmCarro, datalocacao, dataEntrega, vlrDiaria, idVendedor)
SELECT idLocacao, idCliente, idCarro, kmCarro, dataLocacao, vlrDiaria, dataEntrega, idVendedor
FROM tb_locacao 

/*Exibição*/
SELECT * FROM dim_carro;
SELECT * from dim_cliente;
SELECT * FROM dim_dtEntrega;
SELECT * FROM dim_dtLocacao;
SELECT * FROM dim_vendedor;
SELECT * FROM fato_locacao;
