# Solicitar ao usuário uma nota de 0 a 100
nota = float(input("Digite uma nota de 0 a 100: "))

# Classificar a nota de acordo com a escala
if nota >= 90:
    classificacao = "A"
elif nota >= 80:
    classificacao = "B"
elif nota >= 70:
    classificacao = "C"
elif nota >= 60:
    classificacao = "D"
else:
    classificacao = "F"

# Exibir a classificação correspondente
print(f"A classificação da nota é: {classificacao}")
