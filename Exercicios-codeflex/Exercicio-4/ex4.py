import json

# Nome do arquivo JSON
arquivo_json = 'produtos.json'

# Lendo o arquivo JSON
with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
    produtos = json.load(arquivo)

# Exibindo o dicionário Python resultante
print(produtos)
