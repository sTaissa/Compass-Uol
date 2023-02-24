"""
Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.
Dica: leia a documentação da função open(...)

"""

# abre o arquivo com o enconding certo para ler caracteres especiais, lê e fecha o arquivo
with open("sprint3/arquivo_texto.txt", "r", encoding="utf8") as file: 
    print(file.read())
    file.close()
