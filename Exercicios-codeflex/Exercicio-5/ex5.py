import json

# Dicionário com dados de cinco alunos
dados_alunos = {
    "alunos": [
        {"nome": "João", "nota": 8.5},
        {"nome": "Maria", "nota": 9.0},
        {"nome": "Pedro", "nota": 7.0},
        {"nome": "Ana", "nota": 8.0},
        {"nome": "Lucas", "nota": 6.5}
    ]
}

# Caminho do arquivo JSON para salvar os dados dos alunos
caminho_alunos_json = 'alunos.json'

# Gravando o dicionário em um arquivo JSON
with open(caminho_alunos_json, 'w', encoding='utf-8') as arquivo_json:
    json.dump(dados_alunos, arquivo_json, ensure_ascii=False, indent=4)

print("Arquivo JSON 'alunos.json' criado com sucesso!")
