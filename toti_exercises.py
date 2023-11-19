# Faça um programa em Python que peça ao usuário três números inteiros.
# Seu programa deverá passar para uma função os três números (na ordem que foram inseridos pelo usuário) e, então,
# a função deve imprimir o resultado da soma entre o segundo número e o resultado da multiplicação entre o primeiro e último número inseridos. Use como entrada os valores (nessa ordem): 177, 351 e 95.

def operacao_matematica():
  num1 = int(input("Digite o primeiro número: "))
  num2 = int(input("Digite o segundo número: "))
  num3 = int(input("Digite o segundo número: "))
  return (num1 * num3) + num2

operacao_matematica()
