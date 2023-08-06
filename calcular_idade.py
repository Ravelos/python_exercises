"""""
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
"""
import datetime

def calcular_idade(birth_year):
     actual_date = datetime.datetime.now()
     age = actual_date.year - birth_year
     return age
 
def main():
    while True:
        try:
            name=input("Digite seu nome completo: ")
            year=int(input("Digite seu ano de nascimento: "))
            if not 1922<year<2021:
                raise ValueError("Esse ano não está entre 1922 e 2022.")
            age = calcular_idade(year)
            print(name,", você tem ", age, "anos")
            break
        except ValueError as e:
            print(e)
            print("Por favor ingresse un ano valido")
  
main()

