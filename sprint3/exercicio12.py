"""
Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

"""
import json

# abre o arquivo
with open("sprint3/person.json") as file: 
    # converte de json para objeto python, imprime e fecha o arquivo
    data = json.load(file)
    print(data)
    file.close