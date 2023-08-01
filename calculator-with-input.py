"""
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado
"""

def calculator_with_inputs():
  print("1: Soma \n" +"2: Subtração \n" +"3: Multiplicação \n" +"4: Divisão \n" + "0: Sair \n")
  option = int(input("Ingrese a opção: "))
  while option != 0:
    num1= int(input("Ingrese o primeiro número: "))
    num2= int(input("Ingrese o segundo número: "))

    if option == 1:
      return num1 + num2

    elif option == 2:
      return num1 - num2

    elif option == 3:
      return num1  * num2

    elif option == 4:
      return num1 / num2
    else:
      print("Essa opção não existe")

    

