# Author: Helder Henrique da Silva
# Date: 09/03/2023
#
# Descrição: Faça um código em python para dar 20% de desconto para pessoas com mais de 50 anos ou quando o total de compra for maior que R$ 200,00.
#


idade = int(input('Digite sua idade: '))
valorTotal = float(input('Digite o valor total da compra: '))
desconto = 0.2

if idade >= 50 or valorTotal >= 200:
    valorTotal = valorTotal - (valorTotal * desconto)
    print(f'Você tem direito a um desconto de 20% e o valor total da compra é R$ {valorTotal:.2f}')
else:
    print(f'O valor total da compra é R$ {valorTotal:.2f}')
