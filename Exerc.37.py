#Exercicio 37

#037: Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número: '))
binario = bin(num)
octal = oct(num)
hexa = hex(num)

print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'O número {num} convertido para BINÁRIO é {binario [2:]}')
elif opcao == 2:
    print(f'O número {num} convertido para OCTAL é {octal [2:]}')
elif opcao == 3:
    print(f'O número {num} convertido para HEXAGONAL é {hexa [2:]}')
else: 
    print(f'Opção inválida!')




