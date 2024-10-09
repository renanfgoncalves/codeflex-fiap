def encontrar_maximo(numeros):
    # Verifica se a lista está vazia
    if not numeros:
        return None
    # Retorna o maior número da lista
    maximo = max(numeros)
    return maximo

# Testando a função com diferentes listas
lista1 = [10, 20, 30, 40, 50]
lista2 = [5, -7, 9, -11]
lista3 = [3.5, 7.2, 1.8, 9.9, 4.3]
lista4 = []  # Lista vazia

print(f"Maior número em lista1: {encontrar_maximo(lista1)}")
print(f"Maior número em lista2: {encontrar_maximo(lista2)}")
print(f"Maior número em lista3: {encontrar_maximo(lista3)}")
print(f"Maior número em lista4 (vazia): {encontrar_maximo(lista4)}")
