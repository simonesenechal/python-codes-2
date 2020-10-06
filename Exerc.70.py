# Exercicio 70

#070: Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.


print('-' * 40)
print('RESUMO DA COMPRA')
print('-' * 40)

total = count = menor = mil = 0
barato = ' '

while True:
    produto = input('Nome do produto: ')
    preço = float(input('Preço: R$'))
    count += 1
    if preço > 1000:
        mil += 1
    if count == 1 or preço < menor:
        menor = preço
        barato = produto
    total += preço
    ask = ' '
    while ask not in 'NS':
        ask = input('Deseja continuar [S/N]: ').strip().upper()
    if ask == 'N':
        break
print('Calculo finalizado!')
print(f'O total da compra é de R${total:.2f}')
print(f'O {barato} é o produto mais barato, custando R${menor:.2f}.')
print(f'{mil} produtos custam mais de R$1000')



