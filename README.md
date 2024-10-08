# Codeflex

#### (CEO) Alan de Souza Maximiano da Silva - RM557088
#### (Programador) Lancelot Chagas Rodrigues - RM554707
#### (Revisor) André Rovai Andrade Xavier Júnior RM555848
#### (Documentador) Renan de França Gonçalves - RM558413

------------------------------------------------------------------------------------------------------------------------------------------

### Ex:001 - Criação de Matriz 3x3 
Crie uma matriz 3x3 (lista de listas) em Python com valores inteiros de sua escolha e exiba-o no console.

###### Criando a matriz 3x3
`matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]`

###### Exibindo a matriz no console
`for linha in matriz:
    print(linha)`

--------------

### Ex:002 - Multiplicação por Escalar
Crie uma matriz 2x2 e um número escalar. Multiplique cada elemento da matriz pelo escalar e exiba o resultado.

###### Criando uma matriz 2x2, que é uma lista de listas, onde cada lista interna representa uma linha da matriz
`matriz = [
    [2, 4],  # Primeira linha da matriz
    [6, 8]   # Segunda linha da matriz
]`

###### Definindo um número escalar que será usado para multiplicar cada elemento da matriz
escalar = 3

###### Multiplicando cada elemento da matriz pelo escalar
###### Para cada 'linha' na matriz, percorremos os 'elementos' e multiplicamos pelo valor do escalar
`matriz_resultante = [[elemento * escalar for elemento in linha] for linha in matriz]`

###### Exibindo a matriz resultante no console
###### Para cada linha da matriz resultante, imprimimos os valores multiplicados
`for linha in matriz_resultante:
    print(linha)`

------------------------

### Ex:003 - Leitura de Arquivo CSV
Crie um arquivo CSV com três colunas: Nome, Idade, Cidade. Depois, escreva um programa em Python 
import csv  # Importando o módulo 'csv' que permite trabalhar com arquivos CSV (Comma Separated Values)

###### Dados para o CSV 
###### Criamos uma lista de listas, onde cada lista interna representa uma linha a ser escrita no arquivo CSV
`dados = [
    ['Nome', 'Idade', 'Cidade'],  # Cabeçalho (primeira linha do arquivo)
    ['Alice', 25, 'São Paulo'],   # Linha com os dados de Alice
    ['Bruno', 30, 'Rio de Janeiro'],  # Linha com os dados de Bruno
    ['Carla', 22, 'Belo Horizonte']   # Linha com os dados de Carla
]`

###### Criando o arquivo CSV
###### 'w' indica que o arquivo será aberto no modo de escrita (write)
###### 'newline=""' evita a criação de linhas em branco extras ao escrever no arquivo
###### 'encoding="utf-8"' garante que o arquivo seja gravado com a codificação UTF-8, suportando caracteres especiais
`with open('dados.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)  # Criando o objeto 'escritor', que nos permite escrever no arquivo CSV
    escritor.writerows(dados)  # Escreve todas as linhas da lista 'dados' no arquivo de uma vez`

###### Mensagem de confirmação
`print("Arquivo CSV 'dados.csv' criado com sucesso!")`

---

### Ex:004 - Conversão de JSON para Dicionário
Crie um arquivo JSON com informações de uma lista de produtos (nome, preço,
quantidade). Escreva um programa que leia esse arquivo e converta-o em um
dicionário Python.

###### import json  # Importando o módulo 'json', que permite trabalhar com arquivos no formato JSON (JavaScript Object Notation)

###### Nome do arquivo JSON
###### arquivo_json = 'produtos.json'  # Definindo o nome do arquivo JSON que será lido

###### Lendo o arquivo JSON
###### 'r' indica que o arquivo será aberto no modo de leitura (read)
###### 'encoding="utf-8"' garante que o arquivo seja lido com a codificação correta, suportando caracteres especiais
`with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
    produtos = json.load(arquivo)  # Carregando o conteúdo do arquivo JSON e convertendo para um dicionário Python`

###### Exibindo o dicionário Python resultante
`print(produtos)`  # Exibe o conteúdo do arquivo JSON, que agora está em formato de dicionário Python

### Ex:005 - Escrita de Dados em Arquivos JSON
Escrita de Dados em Arquivo JSON
Crie um dicionário Python contendo dados de cinco alunos (nome, nota). Em seguida, grave esse
import json  # Importando o módulo 'json', que permite trabalhar com arquivos no formato JSON (JavaScript Object Notation)

###### Dicionário com dados de cinco alunos, contendo seus nomes e respectivas notas
`dados_alunos = {
    "alunos": [
        {"nome": "João", "nota": 8.5},  # Dados do aluno João
        {"nome": "Maria", "nota": 9.0},  # Dados da aluna Maria
        {"nome": "Pedro", "nota": 7.0},  # Dados do aluno Pedro
        {"nome": "Ana", "nota": 8.0},    # Dados da aluna Ana
        {"nome": "Lucas", "nota": 6.5}   # Dados do aluno Lucas
    ]
}`

###### Caminho do arquivo JSON onde os dados dos alunos serão salvos
`caminho_alunos_json = 'alunos.json'`

###### Gravando o dicionário 'dados_alunos' em um arquivo JSON
###### 'w' indica que o arquivo será aberto no modo de escrita (write)
###### 'encoding="utf-8"' garante que o arquivo seja gravado com a codificação UTF-8, suportando caracteres especiais
###### 'ensure_ascii=False' garante que caracteres especiais (como acentos) sejam preservados
###### 'indent=4' faz com que o JSON seja gravado de forma organizada (com identação)
`with open(caminho_alunos_json, 'w', encoding='utf-8') as arquivo_json:
    json.dump(dados_alunos, arquivo_json, ensure_ascii=False, indent=4)`

###### Mensagem de confirmação
`print("Arquivo JSON 'alunos.json' criado com sucesso!")`

### Ex:006 - Atualização de Dados em CSV
Escreva um programa que leia um arquivo CSV com nomes e idades. Em seguida, permita ao usuário atualizar a idade de uma pessoa e salve a alteração de volta no arquivo CSV.

###### Importa o módulo 'csv' para trabalhar com arquivos CSV (Comma Separated Values)
`import csv`  

###### Caminho do arquivo CSV
`caminho_csv = 'pessoas.csv'`  # Definindo o caminho e o nome do arquivo CSV que será lido e escrito

# Função para ler e exibir o conteúdo do arquivo CSV
def ler_csv(caminho):
    # Abre o arquivo CSV no modo de leitura ('r'), garantindo que a codificação seja UTF-8 e não adicionando novas linhas extras
    with open(caminho, mode='r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)  # Usa DictReader para ler o arquivo como um dicionário, com os títulos das colunas como chaves
        dados = list(leitor)  # Converte o conteúdo lido em uma lista de dicionários
        # Itera sobre cada linha (dicionário) e exibe o nome e idade das pessoas
        for linha in dados:
            print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}")
        return dados  # Retorna os dados lidos para serem utilizados em outras funções

# Função para atualizar a idade de uma pessoa no arquivo CSV
def atualizar_idade(dados, nome, nova_idade):
    # Itera sobre os dados para encontrar a pessoa pelo nome e atualizar a idade
    for linha in dados:
        # Compara os nomes ignorando letras maiúsculas e minúsculas
        if linha['Nome'].lower() == nome.lower():
            linha['Idade'] = nova_idade  # Atualiza a idade da pessoa
            print(f"Idade de {nome} atualizada para {nova_idade}.")  # Exibe mensagem de sucesso
            return True  # Retorna True se a pessoa foi encontrada e atualizada
    print(f"Nome {nome} não encontrado.")  # Mensagem caso o nome não seja encontrado
    return False  # Retorna False se o nome não for encontrado

# Função para salvar os dados atualizados de volta no arquivo CSV
def salvar_csv(caminho, dados):
    # Abre o arquivo CSV no modo de escrita ('w') para sobrescrever o conteúdo
    with open(caminho, mode='w', newline='', encoding='utf-8') as arquivo:
        campos = ['Nome', 'Idade']  # Define as colunas do arquivo (campo 'Nome' e campo 'Idade')
        escritor = csv.DictWriter(arquivo, fieldnames=campos)  # Cria um escritor CSV que escreverá dicionários com base nos campos definidos
        escritor.writeheader()  # Escreve a linha de cabeçalho (títulos das colunas)
        escritor.writerows(dados)  # Escreve todas as linhas de dados (já com as atualizações) no arquivo CSV

# Programa principal
if __name​⬤

### Ex:007 - Conectar ao MongoDB
Escreva um programa em Python que se conecte a um banco de dados MongoDB local e exiba uma lista dos bancos de dados disponíveis.

###### Importando MongoClient, que permite conectar-se a um servidor MongoDB
`from pymongo import MongoClient`  
###### Conectar ao servidor MongoDB local
###### O MongoClient cria uma conexão com o servidor MongoDB rodando no endereço 'localhost' (127.0.0.1) e na porta padrão 27017
`cliente = MongoClient('mongodb://localhost:27017/')`

###### Listar todos os bancos de dados disponíveis no servidor MongoDB ao qual estamos conectados
`bancos_de_dados = cliente.list_database_names()`

###### Exibir a lista de bancos de dados
`print("Bancos de dados disponíveis:")
for banco in bancos_de_dados:  # Itera sobre cada banco de dados listado
    print(f"- {banco}")  # Exibe o nome de cada banco de dados encontrado`

###### Fechar a conexão
###### Fecha a conexão com o servidor MongoDB, liberando recursos
`cliente.close()`

### Ex:008 - 

### Ex:009 - 

### Ex:010 - 

### Ex:011 - 

### Ex:012 - 

### Ex:013 - 

### Ex:014 - 

### Ex:015 - 

### Ex:016 - 

### Ex:017 - 

### Ex:018 - 

### Ex:019 - 

### Ex:020 - 
