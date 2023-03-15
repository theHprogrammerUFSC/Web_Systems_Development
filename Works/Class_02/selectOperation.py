# Author: Helder Henrique da Silva
# Date: 09/03/2023
#
# Descrição: Escreva um programa que leia dois núumeros e pergunte qual operação deseja realizar.
# As operações disvoníveis para escolha deverão ser: soma (+), subtração (-), multiplicação (*) e divisão (/).
# Exiba o resultado da operação solicitada
#

# Soma dois números
def soma (a, b):
    return a + b

# Subtrai dois números
def subtracao (a, b):
    return a - b

# Multiplica dois números
def multiplicacao (a, b):
    return a * b

# Divide dois números
def divisao (a, b):
    return a / b

# Função principal
def main():
    print('-=-' * 20)
    print('CALCULADORA')
    print('-=-' * 20)

    # Entrada de dados
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    
    menu = '''
    Escolha a operação desejada:
    + para Soma
    - para Subtração
    * para Multiplicação
    / para Divisão
    '''
    
    print('\n', menu, '\n')
    
    operacao = input('Digite a operação desejada: ')

    # Processamento
    if operacao == '+':
        resultado = soma(num1, num2)
    elif operacao == '-':
        resultado = subtracao(num1, num2)
    elif operacao == '*':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/':
        resultado = divisao(num1, num2)
    else:
        print('Operação inválida!')

    # Saída de dados
    print(f'O resultado da operação é {resultado:.2f}')

# Chamada da função principal
main()

