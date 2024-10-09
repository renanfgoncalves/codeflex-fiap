from pymongo import MongoClient

# Conectar ao servidor MongoDB local
cliente = MongoClient('mongodb://localhost:27017/')

# Listar todos os bancos de dados disponíveis
bancos_de_dados = cliente.list_database_names()

# Exibir a lista de bancos de dados
print("Bancos de dados disponíveis:")
for banco in bancos_de_dados:
    print(f"- {banco}")

# Fechar a conexão
cliente.close()
