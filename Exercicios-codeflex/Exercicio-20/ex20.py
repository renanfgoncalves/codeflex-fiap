def converter_temperatura(celsius, tipo="F"):
    # Converte para Fahrenheit se o tipo for "F" ou se não for especificado
    if tipo == "F":
        return (celsius * 9/5) + 32
    # Converte para Kelvin se o tipo for "K"
    elif tipo == "K":
        return celsius + 273.15
    else:
        # Retorna None se um tipo inválido for fornecido
        return None

# Testando a função com diferentes valores e tipos
print(converter_temperatura(25))  # Padrão: Fahrenheit
print(converter_temperatura(25, "F"))  # Fahrenheit
print(converter_temperatura(25, "K"))  # Kelvin
print(converter_temperatura(25, "X"))  # Tipo inválido
