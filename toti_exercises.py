# Faça um programa em Python que peça ao usuário três números inteiros.
# Seu programa deverá passar para uma função os três números (na ordem que foram inseridos pelo usuário) e, então,
# a função deve imprimir o resultado da soma entre o segundo número e o resultado da multiplicação entre o primeiro e último número inseridos. Use como entrada os valores (nessa ordem): 177, 351 e 95.

def operacao_matematica():
  num1 = int(input("Digite o primeiro número: "))
  num2 = int(input("Digite o segundo número: "))
  num3 = int(input("Digite o segundo número: "))
  return (num1 * num3) + num2

operacao_matematica()

# De acordo com a fórmula da equação de segundo grau abaixo. Faça uma função que calcule e imprima os resultados de uma equação de segundo grau.
# Para que seu código fique organizado, faça uma função extra que calcule o Delta () em seprado. Utilize os seguintes valores como entrada: a = 88, b = 4, c = 16

def calcula_delta(a, b , c):
  if a is None:
    a = float(input("Digite o valor de a: "))
  elif b is None:
    b = float(input("Digite o valor de b: "))
  elif c is None:
    c = float(input("Digite o valor de c: "))
  else:
    return (b**2) - (4 * a * c)

def ecuacao_segundo_grau():
  a = float(input("Digite o valor de a: "))
  b = float(input("Digite o valor de b: "))
  c = float(input("Digite o valor de c: "))
  delta = calcula_delta(a, b, c)
  x1 = (-b + (delta ** 0.5)) / (2* a)
  x2 = (-b - (delta ** 0.5)) / (2* a)
  print("O valor de x1 é : ", x1);
  print("O valor de x2 é : " , x2);

ecuacao_segundo_grau()
