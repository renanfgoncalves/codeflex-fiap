import csv

# Dados para o CSV
dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['Alice', 25, 'São Paulo'],
    ['Bruno', 30, 'Rio de Janeiro'],
    ['Carla', 22, 'Belo Horizonte']
]

# Criando o arquivo CSV
with open('dados.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)

print("Arquivo CSV 'dados.csv' criado com sucesso!")