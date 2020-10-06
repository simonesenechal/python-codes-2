# Exercicio 59

# 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. 

valor_1 = int(input('Primeiro valor: '))
valor_2 = int(input('Segundo valor: '))

print(' ')

opcao = 0

while opcao != 5:
    print('''Escolha uma opção:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('Qual a opção escolhida? '))
    if opcao == 1:
        soma = valor_1 + valor_2
        print(f'\nA soma entre {valor_1} e {valor_2} é igual {soma}')
    elif opcao == 2:
        multi = valor_1 * valor_2
        print(f'\nA multiplicação entre {valor_1} e {valor_2} é igual {multi}')
    elif opcao == 3:
        if valor_1 < valor_2:
            print(f'\nO maior valor é {valor_2}')
        else: 
            print(f'\nO maior valor é {valor_1}')
    elif opcao == 4:
        valor_1 = int(input('Primeiro valor: '))
        valor_2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print(f'\nFinalizando...')
    else:
        print('\nOpção inválida!')

    



    








