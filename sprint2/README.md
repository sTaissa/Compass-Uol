<h1 align="center"> Sprint 2</h1>

<p align="center">
 <a href="#exercicio-b">Exercícios SQL Biblioteca</a> •
 <a href="#exercicio-l">Exercícios SQL Loja</a>
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

&nbsp;
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

&nbsp;
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

&nbsp;
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

&nbsp;
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

&nbsp;
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

&nbsp;
![saída exercício 7](https://github.com/sTaissa/Compass-Uol/blob/main/sprint2/imagens-sprint2/e7.PNG)

<br>

<a id="exercicio-b"></a>
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

&nbsp;
![saída exercício 8](/sprint2/imagens-sprint2/e8.PNG)