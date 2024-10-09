from pymongo import MongoClient

# Conectar ao servidor MongoDB local
cliente = MongoClient('mongodb://localhost:27017/')

# Acessar o banco de dados 'escola' e a coleção 'alunos'
db = cliente['escola']
colecao_alunos = db['alunos']

# Solicitar o nome do aluno para exclusão
nome_aluno = input("Digite o nome do aluno que deseja remover: ")

# Remover o documento com base no nome
resultado = colecao_alunos.delete_one({"nome": nome_aluno})

# Verificar se o documento foi removido
if resultado.deleted_count > 0:
    print(f"O aluno '{nome_aluno}' foi removido com sucesso.")
else:
    print(f"Nenhum aluno com o nome '{nome_aluno}' foi encontrado.")

# Fechar a conexão
cliente.close()
