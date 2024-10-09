def calcular_media(numeros):
    # Verifica se a lista está vazia para evitar divisão por zero
    if len(numeros) == 0:
        return 0
    # Calcula a média dos números
    media = sum(numeros) / len(numeros)
    return media

# Testando a função com diferentes listas
lista1 = [10, 20, 30, 40, 50]
lista2 = [5, 7, 9, 11]
lista3 = [3.5, 7.2, 1.8, 9.9, 4.3]
lista4 = []  # Lista vazia

print(f"Média de lista1: {calcular_media(lista1)}")
print(f"Média de lista2: {calcular_media(lista2)}")
print(f"Média de lista3: {calcular_media(lista3)}")
print(f"Média de lista4 (vazia): {calcular_media(lista4)}")
