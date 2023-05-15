/*Criação das tabelas para normalização*/

CREATE TABLE tb_pais (
idPais INTEGER PRIMARY KEY AUTOINCREMENT,
nomePais VARCHAR(40)
);

CREATE TABLE tb_estado (
idEstado INTEGER PRIMARY KEY AUTOINCREMENT,
nomeEstado VARCHAR(40),
idPais INT,
CONSTRAINT idPais FOREIGN KEY (idPais) REFERENCES tb_pais(idPais)
);

CREATE TABLE tb_cidade (
idCidade INTEGER PRIMARY KEY AUTOINCREMENT,
nomeCidade VARCHAR(40),
idEstado INT,
CONSTRAINT idEstado FOREIGN KEY (idEstado) REFERENCES tb_estado(idEstado)
);
 
CREATE TABLE tb_cliente (
idCliente INT PRIMARY KEY,
nomeCliente VARCHAR(100),
idCidade INT,
CONSTRAINT idCidade FOREIGN KEY (idCidade) REFERENCES tb_cidade(idCidade)
);

CREATE TABLE tb_vendedor (
idVendedor INT PRIMARY KEY,
nomeVendedor VARCHAR(100),
sexoVendedor CHAR(1),
idEstado INT,
CONSTRAINT idEstado FOREIGN KEY (idEstado) REFERENCES tb_estado(idEstado)
);

CREATE TABLE tb_marcaCarro (
idMarca INTEGER PRIMARY KEY AUTOINCREMENT,
nomeMarca VARCHAR(80)
);

CREATE TABLE tb_modeloCarro (
idModelo INTEGER PRIMARY KEY AUTOINCREMENT,
idMarca INT,
nomeModelo VARCHAR(80),
CONSTRAINT idMarca FOREIGN KEY (idMarca) REFERENCES tb_marcaCarro(idMarca)
);

CREATE TABLE tb_combustivel (
idCombustivel INT PRIMARY KEY,
tipoCombustivel VARCHAR(20)
);

CREATE TABLE tb_carro (
idCarro INT PRIMARY KEY, 
classiCarro VARCHAR(50),
idModelo INT,
anoCarro INT,
idCombustivel INT,
CONSTRAINT idModelo FOREIGN KEY (idModelo) REFERENCES tb_modeloCarro(idModelo),
CONSTRAINT idCombustivel FOREIGN KEY (idCombustivel) REFERENCES tb_combustivel(idCombustivel)
);


/*Inserção dos dados nas novas tabelas para a normalização*/

INSERT INTO tb_pais (nomePais) VALUES ('Brasil');

INSERT INTO tb_estado (nomeEstado, idPais) 
SELECT DISTINCT estadoCliente, 1 FROM tb_locacao; 

INSERT INTO tb_cidade (nomeCidade, idEstado) 
SELECT DISTINCT l.cidadeCliente, e.idEstado 
FROM tb_locacao AS l
INNER JOIN tb_estado AS e
	ON l.estadoCliente = e.nomeEstado;

INSERT INTO tb_cliente (idCliente, nomeCliente , idCidade) 
SELECT DISTINCT l.idCliente, l.nomeCliente, c.idCidade
FROM tb_locacao AS l 
INNER JOIN tb_cidade AS c
	ON l.cidadeCliente  = c.nomeCidade;
	
INSERT INTO tb_vendedor (idVendedor, nomeVendedor, sexoVendedor, idEstado) 
SELECT DISTINCT l.idVendedor, l.nomeVendedor, l.sexoVendedor, e.idEstado
FROM tb_locacao AS l
INNER JOIN tb_estado AS e
	ON l.estadoVendedor = e.nomeEstado;

INSERT INTO tb_marcaCarro (nomeMarca) 
SELECT DISTINCT l.marcaCarro 
FROM tb_locacao AS l;

INSERT INTO tb_modeloCarro (idMarca, nomeModelo) 
SELECT DISTINCT m.idMarca, l.modeloCarro
FROM tb_locacao AS l
INNER JOIN tb_marcaCarro AS m
	ON l.marcaCarro = m.nomeMarca;

INSERT INTO tb_combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel FROM tb_locacao; 

INSERT INTO tb_carro (idCarro, classiCarro, idModelo, anoCarro, idCombustivel)
SELECT DISTINCT l.idCarro, l.classiCarro, m.idModelo, l.anoCarro, l.idCombustivel
FROM tb_locacao AS l
INNER JOIN tb_modeloCarro AS m 
	ON l.modeloCarro = m.nomeModelo;
	

/*Atualização tabela locacao após a normalização

- Alter table add constraint não funcionou então criei uma nova tabela
- Apesar de kmCarro estar relacionado ao carro, é um valor que muda constantemente a cada locacao, então fazendo uma análise decidi 
deixar o atributo na tabela locacao, ficando assim registrado a quilometragem do carro no momento da locacao*/

CREATE TABLE tb_locacao1 (
idLocacao INTEGER PRIMARY KEY AUTOINCREMENT,
idCliente INT,
idCarro INT,
kmCarro INT,
dataLocacao DATETIME,
horaLocacao TIME,
vlrDiaria DECIMAL(18,2),
dataEntrega DATE,
horaEntrega TIME,
idVendedor VARCHAR(100),
CONSTRAINT idCliente FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
CONSTRAINT idCarro FOREIGN KEY (idCarro) REFERENCES tb_carro(idCarro),
CONSTRAINT idVendedor FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor)
);

INSERT INTO tb_locacao1 (idLocacao, idCliente, idCarro, kmCarro, dataLocacao, horaLocacao, vlrDiaria, dataEntrega, horaEntrega, idVendedor)
SELECT DISTINCT idLocacao, idCliente, idCarro, kmCarro, dataLocacao, horaLocacao, vlrDiaria, dataEntrega, horaEntrega, idVendedor
FROM tb_locacao;

DROP TABLE tb_locacao;

ALTER TABLE tb_locacao1 RENAME TO tb_locacao

/*Trata os dados/*

/*Tira as vírgulas e separa cada parte da data, passando-as como argumento para a strftime tranformar em datetime certinho*/
UPDATE tb_locacao  SET dataLocacao = strftime('%Y-%m-%d', substr(replace(dataLocacao, ',', ''),1,4)||'-'||substr(dataLocacao,5,2)||'-'||substr(dataLocacao,7,2));
UPDATE tb_locacao  SET dataEntrega = strftime('%Y-%m-%d', substr(replace(dataEntrega, ',', ''),1,4)||'-'||substr(dataEntrega,5,2)||'-'||substr(dataEntrega,7,2));

/*Substitui 0 e 1 em sexo do vendedor por "F" ou "M"*/
UPDATE tb_vendedor SET sexoVendedor = 
CASE
	WHEN sexoVendedor = 0 THEN "F"
	WHEN sexoVendedor = 1 THEN "M"
END

/*Exibição*/
SELECT * FROM tb_pais;
SELECT * FROM tb_estado;
SELECT * FROM tb_cidade;
SELECT * FROM tb_cliente;
SELECT * FROM tb_vendedor;
SELECT * FROM tb_combustivel;
SELECT * FROM tb_marcaCarro;
SELECT * FROM tb_modeloCarro;
SELECT * FROM tb_carro;
SELECT * FROM tb_locacao;
