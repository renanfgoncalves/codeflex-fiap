import csv

# Caminho do arquivo CSV
caminho_csv = 'pessoas.csv'

# Função para ler e exibir o conteúdo do arquivo CSV
def ler_csv(caminho):
    with open(caminho, mode='r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        dados = list(leitor)
        for linha in dados:
            print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}")
        return dados

# Função para atualizar a idade de uma pessoa
def atualizar_idade(dados, nome, nova_idade):
    for linha in dados:
        if linha['Nome'].lower() == nome.lower():
            linha['Idade'] = nova_idade
            print(f"Idade de {nome} atualizada para {nova_idade}.")
            return True
    print(f"Nome {nome} não encontrado.")
    return False

# Função para salvar os dados atualizados de volta no CSV
def salvar_csv(caminho, dados):
    with open(caminho, mode='w', newline='', encoding='utf-8') as arquivo:
        campos = ['Nome', 'Idade']
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(dados)

# Programa principal
if __name__ == "__main__":
    # Lendo o arquivo CSV e exibindo o conteúdo
    print("Conteúdo do arquivo CSV:")
    dados_pessoas = ler_csv(caminho_csv)
    
    # Solicitando o nome da pessoa e a nova idade
    nome_pessoa = input("\nDigite o nome da pessoa para atualizar a idade: ")
    nova_idade = input("Digite a nova idade: ")

    # Atualizando a idade
    if atualizar_idade(dados_pessoas, nome_pessoa, nova_idade):
        # Salvando as alterações de volta no arquivo CSV
        salvar_csv(caminho_csv, dados_pessoas)
        print("\nArquivo CSV atualizado com sucesso!")
    else:
        print("\nNenhuma alteração foi feita.")
