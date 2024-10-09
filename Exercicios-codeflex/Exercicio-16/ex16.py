def celsius_para_fahrenheit(celsius):
    # Fórmula de conversão de Celsius para Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Exemplo de uso da função
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius} graus Celsius é igual a {temperatura_fahrenheit} graus Fahrenheit.")
