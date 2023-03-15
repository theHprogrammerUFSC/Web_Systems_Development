# Author: Helder Henrique da Silva
# Date: 09/03/2023
#
# Descrição: Escreve um programa que receba 3 números como entrada, seu programa deve informar qual número é o maior e qual é o menor.
#

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        menor = n3
    else:
        menor = n2
elif n2 > n1 and n2 > n3:
    maior = n2
    if n1 > n3:
        menor = n3
    else:
        menor = n1
else:
    maior = n3
    if n1 > n2:
        menor = n2
    else:
        menor = n1
        
print(f'O maior número é {maior} e o menor é {menor}')
