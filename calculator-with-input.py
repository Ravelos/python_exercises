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


def calculator_with_input():
  opcoes = [
    "Soma",
    "Subtração",
    "Multiplicação",
    "Divisão",
    "Sair"
  ]

  while True:
    for indice, opcao in enumerate(opcoes):
        print(f"{indice}: {opcao}")
    selecao = int(input("Digite o número da opção:" ))

    if selecao == 0:
      print("Saindo.")
      print("Saindo..")
      print("Saindo...")
      break
    elif selecao == 1:
      num1 = int(input("Digite o primeiro número: "))
      num2 = int(input("Digite o segundo número: "))
      res = num1 + num2
      print(res)
    elif selecao == 2:
      num1 = int(input("Digite o primeiro número: "))
      num2 = int(input("Digite o segundo número: "))
      res = num1 - num2
      print(res)
    elif selecao == 3:
      num1 = int(input("Digite o primeiro número: "))
      num2 = int(input("Digite o segundo número: "))
      res = num1 * num2
      print(res)
    elif selecao == 4:
      num1 = int(input("Digite o primeiro número: "))
      num2 = int(input("Digite o segundo número: "))
      res = num1 / num2
      print(res)
    else:
      print("Opção inválida. Tente novamente.")
    
    
calculator_with_input()    
  


    

