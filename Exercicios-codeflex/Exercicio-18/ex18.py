def contar_vogais(texto):
    # Definindo as vogais
    vogais = "aeiouAEIOU"
    # Contando as vogais na string
    contador = sum(1 for letra in texto if letra in vogais)
    return contador

# Testando a função com diferentes strings
teste1 = "Olá, como vai você?"
teste2 = "Python é incrível!"
teste3 = "12345"
teste4 = "AEIOU aeiou"

print(f"Quantidade de vogais em teste1: {contar_vogais(teste1)}")
print(f"Quantidade de vogais em teste2: {contar_vogais(teste2)}")
print(f"Quantidade de vogais em teste3: {contar_vogais(teste3)}")
print(f"Quantidade de vogais em teste4: {contar_vogais(teste4)}")
