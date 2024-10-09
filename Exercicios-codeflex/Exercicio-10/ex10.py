from pymongo import MongoClient

# Conectar ao servidor MongoDB local
mongo_client = MongoClient('mongodb://localhost:27017/')

# Acessar o banco de dados 'empresa' e a coleção 'clientes'
db = mongo_client['empresa']
colecao_clientes = db['clientes']

# Consultar todos os clientes com idade superior a 30 anos
clientes_acima_de_30 = colecao_clientes.find({"idade": {"$gt": 30}})

# Exibir os clientes encontrados
print("Clientes com idade superior a 30 anos:")
for cliente in clientes_acima_de_30:
    print(f"Nome: {cliente['nome']}, Idade: {cliente['idade']}")

# Fechar a conexão com o MongoDB
mongo_client.close()
