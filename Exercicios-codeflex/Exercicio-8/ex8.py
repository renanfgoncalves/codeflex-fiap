from pymongo import MongoClient

# Conectar ao servidor MongoDB local
cliente = MongoClient('mongodb://localhost:27017/')

# Acessar o banco de dados 'escola' e a coleção 'alunos'
db = cliente['escola']
colecao_alunos = db['alunos']

# Consultar todos os documentos na coleção 'alunos'
alunos = colecao_alunos.find()

# Exibir cada documento no console
print("Lista de alunos:")
for aluno in alunos:
    print(aluno)

# Fechar a conexão
cliente.close()
