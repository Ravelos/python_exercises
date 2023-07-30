"""
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
"""

def calculator(num1, num2, operacao):

    if operacao == "soma":
        resultado = num1 + num2
        print(resultado)

    elif operacao == "subtração":
        resultado = num1 - num2
        print(resultado)

    elif operacao == "multiplicacao":
        resultado = num1 * num2
        print(resultado)

    elif operacao == "divisão":
        resultado = num1 / num2
        print(resultado)
    else:
        print("Operação não permitida")

calculator(1,5, "divisão")
