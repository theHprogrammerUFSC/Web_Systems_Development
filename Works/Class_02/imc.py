# Author: Helder Henrique da Silva
# Date: 09/03/2023
#
# Descrição: Programa para calcular o IMC de uma pessoa
# Calculo do IMC: peso / (altura * altura)
#

print('-=-' * 20)
print('CALCULADORA DE IMC')
print('-=-' * 20)

peso = float(input('\nDigite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura * altura)

print(f'Seu IMC é {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade mórbida!')