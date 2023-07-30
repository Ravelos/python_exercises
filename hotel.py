"""
Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
"""

andar = 0

for i in range(20):
    andar += 1
    if andar == 13:
     continue
    print (andar)

# Segunda solução

andar_solution2 = 0

while andar_solution2 <= 21:
    andar_solution2 += 1
    if andar_solution2 == 13:
        continue
    print(andar_solution2)


# 3era soluçaõ

andar_solution3 = 0

for andar_solution3 in range(1,21):
    if andar_solution3 == 13:
        continue
    print(andar_solution3)




