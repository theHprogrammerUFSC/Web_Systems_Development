# Author: Helder Henrique da Silva
# Date: 14/03/2023
#
# Descrição: Faça um programa que receba a lista a seguir e coloque em ordem crescente. 

Lista = [2,12,20,0,1,3,40,7,5,10]

print(f'Lista original: {Lista}')

for i in range(len(Lista)):
    for j in range(i+1, len(Lista)):
        if Lista[i] > Lista[j]:
            Lista[i], Lista[j] = Lista[j], Lista[i]

print(f'Lista ordenada: {Lista}')

