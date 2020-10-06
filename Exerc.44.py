#Exercicio 44

#044: Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

valor = float(input('Qual o valor do produto? '))

print('''FORMAS DE PAGAMENTO
[1] Á vista dinheiro/cheque
[2] Cartão de crédito á vista
[3] Cartão parcelado em até 2x
[4] Cartão parcelado acima de 3x''')

opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    total = valor - (valor * 0.1)
    print(f'Você ganhou 10% de desconto. O valor a ser pago é de R${total:.2f}.')
elif opcao == 2:
    total1 = valor - (valor * 0.05)
    print(f'Você ganhou 5% de desconto. O valor a ser pago é de R${total1:.2f}.')
elif opcao == 3:
    print(f'O valor a ser pago é de {valor:.2f}, divido em 2x.')
elif opcao == 4:
    total2 = valor + (valor * 0.2)
    parcela = int(input('Qual o total das parcelas? '))
    print(f'Haverá o acréscimo de 20%. O valor a ser pago é \
de R${total2:.2f}, dividido em {parcela} parcelas')
else:
    print('Opção inválida, tente novamente!')

    






