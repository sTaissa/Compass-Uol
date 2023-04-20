"""
Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.
Dica: leia a documentação da função open(...)

"""

# abre o arquivo com o enconding certo para ler caracteres especiais, lê e fecha o arquivo
with open("sprint3/exercicios/arquivo_texto.txt", "r", encoding="utf8") as file: 
    # print sempre termina com quebra de linha, a menos que coloque "end" como nulo 
    print(file.read())
    file.close()
