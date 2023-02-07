--- E1: Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, 
--- as linhas. Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, 
--- idioma
SELECT * --- As colunas pedidas são iguais as originais da tabela
FROM livro
WHERE publicacao  > '2014-12-31'
ORDER BY cod ASC


--- E2:Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.
--- Atenção às colunas esperadas no resultado final:  titulo, valor.
SELECT titulo, valor
FROM livro
ORDER BY valor DESC --- Ordena do mais caro ao mais barato
LIMIT 10 --- Limita aos 10 mais caros


--- E3: Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as 
--- colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros 
--- em ordem decrescente.
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


--- E4: Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela 
--- coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e 
--- quantidade (total de livros de sua autoria).
SELECT au.nome, au.codautor, au.nascimento, COUNT(li.cod) AS quantidade --- Conta a quantidade de livros da tabela livros relacionado a cada autor da tabela autor
FROM autor AS au
LEFT JOIN livro AS li
	ON li.autor = au.codautor 
GROUP BY au.nome, au.codautor, au.nascimento 
ORDER BY au.nome ASC -- Ordena alfabeticamente


--- E5: Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na 
--- região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente.
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


--- E6: Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter 
--- apenas as colunas codautor, nome, quantidade_publicacoes.
SELECT au.codautor, au.nome, COUNT(*) AS quantidade_publicacoes --- Conta todos os livros por autor
FROM livro AS li
LEFT JOIN autor AS au 
	ON li.autor = au.codautor 
GROUP BY au.codautor, au.nome
ORDER BY quantidade_publicacoes DESC --- Lista do mais caro ao mais barato
LIMIT 1 --- Limita ao primeiro mais caro


--- E7: Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.
SELECT nome
FROM autor AS au
LEFT JOIN livro AS li 
	ON au.codautor = li.autor
WHERE li.autor IS NULL --- Mostra apenas os autores que não tem correspondentes na tabela livros
ORDER BY autor ASC