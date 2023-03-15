# Author: Helder Henrique da Silva
# Date: 14/03/2023
#
# Descrição: Faça um programa em Python que receba uma lista com 10 valores inteiros e mostre para o usuário qual número é o maior e qual é o menor.

list = [10, 50, 20, 100, 30, 90, 45, 84, 2, 61]

print('A lista é:', list)

maior = list[0]
menor = list[0]

for i in range(1, len(list)):
    if list[i] > maior:
        maior = list[i]
    if list[i] < menor:
        menor = list[i]

print(f'O maior número é {maior} e o menor é {menor}')


