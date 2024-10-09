# Criando a matriz 2x2
matriz = [
    [2, 4],
    [6, 8]
]

# Definindo um número escalar
escalar = 3

# Multiplicando cada elemento da matriz pelo escalar
matriz_resultante = [[elemento * escalar for elemento in linha] for linha in matriz]

# Exibindo a matriz resultante no console
for linha in matriz_resultante:
    print(linha)
