# Author: Helder Henrique da Silva
# Date: 14/03/2023
#
# Descrição: Faça um programa em Python para exibir a tabuada de 0 a 9.

print('-=-'*20)
print('Tabuada de 0 a 9')
print('-=-'*20)

for i in range(10):
    print('\nTabuada do', i)
    for j in range(11):
        print(f'{i} x {j} = {i*j}')
    print('\n')
