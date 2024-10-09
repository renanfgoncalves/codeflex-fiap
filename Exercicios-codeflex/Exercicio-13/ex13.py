# Solicitar ao usuário sua idade
idade = int(input("Digite sua idade: "))

# Classificar a pessoa na faixa etária correspondente
if idade < 12:
    classificacao = "Criança"
elif 12 <= idade <= 17:
    classificacao = "Adolescente"
elif 18 <= idade <= 64:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

# Exibir a classificação etária
print(f"Você é classificado como: {classificacao}")
