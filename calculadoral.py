def calcular(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return nume1 * num2
    elif operacao == '/':
        if num2 == 0 :
            return "erro: divisão por zero"
        else:
            return "Operação inválida!"

        # Entrada do usuário
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        # Chamada da função e exibição do resultado
        resultado = calcular(num1, num2, operacao)
        print(f"Resultado: {resultado}")
