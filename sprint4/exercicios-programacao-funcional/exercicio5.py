"""
Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do arquivo corresponde ao 
nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.

Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:
Nome do estudante
Três maiores notas, em ordem decrescente
Média das três maiores notas, com duas casas decimais de precisão

O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao 
formato descrito a seguir:
Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>

Exemplo:
Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67
Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33

Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:
round
map
sorted

"""
import csv

# extrai os dados do arquivo e joga numa lista(num)
def extrai(caminho):
    file = open(caminho, encoding="utf-8")
    num = csv.reader(file)

    # filtra e retorna os valores pedidos
    def filtra():
        # função a ser passada no map, recebe uma lista (nome e 5 notas de uma aluno) e retorna uma lista já filtrada com apenas o nome e as 3 maiores notas
        def func(x):
            # transforma as 5 notas em int
            notas = list(map(lambda x: int(x), x[1:6]))
            # ordena pela maior nota
            notas = sorted(notas, reverse=True)
            # cria lista com o nome do aluno eas 3 maiores notas
            lista = [x[0], notas[:3]]
            return lista

        # aplica a função a cada aluno da lista e oredena pelo nome do aluno
        lista = sorted(list(map(func, num)))

        # retorna o relatório textual para cada aluno
        # a média é a soma das 3 notas / pelo tamamnho da lista e arredondado pra 2 casas
        file.close()
        return list(map(lambda x: print(f"Nome: {x[0]} Notas: {x[1]} Média: {round(sum(x[1])/len(x[1]), 2)}"), lista))
    return filtra()

extrai("sprint4/exercicios-programacao-funcional/estudantes.csv")