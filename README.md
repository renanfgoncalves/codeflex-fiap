# Codeflex

#### (CEO) Alan de Souza Maximiano da Silva - RM557088
#### (Programador) Lancelot Chagas Rodrigues - RM554707
#### (Revisor) André Rovai Andrade Xavier Júnior RM555848
#### (Documentador) Renan de França Gonçalves - RM558413

------------------------------------------------------------------------------------------------------------------------------------------

### Ex:001 - Criação de Matriz 3x3 
Crie uma matriz 3x3 (lista de listas) em Python com valores inteiros de sua escolha e exiba-o no console.

Criando a matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Exibindo a matriz no console
for linha in matriz:
    print(linha)

--------------

### Ex:002 - Multiplicação por Escalar
Crie uma matriz 2x2 e um número escalar. Multiplique cada elemento da matriz pelo escalar e exiba o resultado.

Criando uma matriz 2x2, que é uma lista de listas, onde cada lista interna representa uma linha da matriz
matriz = [
    [2, 4],  # Primeira linha da matriz
    [6, 8]   # Segunda linha da matriz
]

##### Definindo um número escalar que será usado para multiplicar cada elemento da matriz
escalar = 3

##### Multiplicando cada elemento da matriz pelo escalar
##### Para cada 'linha' na matriz, percorremos os 'elementos' e multiplicamos pelo valor do escalar
matriz_resultante = [[elemento * escalar for elemento in linha] for linha in matriz]

##### Exibindo a matriz resultante no console
##### Para cada linha da matriz resultante, imprimimos os valores multiplicados
for linha in matriz_resultante:
    print(linha)

------------------------

### Ex:003 - Leitura de Arquivo CSV
Crie um arquivo CSV com três colunas: Nome, Idade, Cidade. Depois, escreva um programa em Python 
import csv  # Importando o módulo 'csv' que permite trabalhar com arquivos CSV (Comma Separated Values)

##### Dados para o CSV
##### Criamos uma lista de listas, onde cada lista interna representa uma linha a ser escrita no arquivo CSV
dados = [
    ['Nome', 'Idade', 'Cidade'],  # Cabeçalho (primeira linha do arquivo)
    ['Alice', 25, 'São Paulo'],   # Linha com os dados de Alice
    ['Bruno', 30, 'Rio de Janeiro'],  # Linha com os dados de Bruno
    ['Carla', 22, 'Belo Horizonte']   # Linha com os dados de Carla
]

##### Criando o arquivo CSV
##### 'w' indica que o arquivo será aberto no modo de escrita (write)
##### 'newline=""' evita a criação de linhas em branco extras ao escrever no arquivo
##### 'encoding="utf-8"' garante que o arquivo seja gravado com a codificação UTF-8, suportando caracteres especiais
with open('dados.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)  # Criando o objeto 'escritor', que nos permite escrever no arquivo CSV
    escritor.writerows(dados)  # Escreve todas as linhas da lista 'dados' no arquivo de uma vez

##### Mensagem de confirmação
print("Arquivo CSV 'dados.csv' criado com sucesso!")

---

### Ex:004 - Conversão de JSON para Dicionário
Crie um arquivo JSON com informações de uma lista de produtos (nome, preço,
quantidade). Escreva um programa que leia esse arquivo e converta-o em um
dicionário Python.

import json  # Importando o módulo 'json', que permite trabalhar com arquivos no formato JSON (JavaScript Object Notation)

# Nome do arquivo JSON
arquivo_json = 'produtos.json'  # Definindo o nome do arquivo JSON que será lido

# Lendo o arquivo JSON
# 'r' indica que o arquivo será aberto no modo de leitura (read)
# 'encoding="utf-8"' garante que o arquivo seja lido com a codificação correta, suportando caracteres especiais
with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
    produtos = json.load(arquivo)  # Carregando o conteúdo do arquivo JSON e convertendo para um dicionário Python

# Exibindo o dicionário Python resultante
print(produtos)  # Exibe o conteúdo do arquivo JSON, que agora está em formato de dicionário Python

### Ex:005 - Escrita de Dados em Arquivos JSON

### Ex:006 - 

### Ex:007 - 

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


