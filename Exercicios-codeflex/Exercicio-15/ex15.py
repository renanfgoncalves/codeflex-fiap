# Solicitar ao usuário dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Solicitar ao usuário a operação matemática
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Realizar a operação com base na entrada do usuário
if operacao == '+':
    resultado = numero1 + numero2
    print(f"O resultado da soma é: {resultado}")
elif operacao == '-':
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == '*':
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha +, -, * ou /.")
