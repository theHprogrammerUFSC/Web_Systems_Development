# Author: Helder Henrique da Silva
# Date: 09/03/2023
#
# Descrição: Escreva um programa que leia a média final e a porcentagem de frequência de um aluno e informe se ele está aprovado, reprovado por nota ou reprovado por falta.
# Considerações: A média de aprovação deve ser maior ou igual a 6, e a frequência maior ou igual a 75%.
#

media = float(input('Digite a média final: '))
frequencia = int(input('Digite a frequência: '))

if media >= 6:
    if frequencia >= 75:
        print('Aprovado')
    else:
        print('Reprovado por falta')
else:
    print('Reprovado por nota')
    