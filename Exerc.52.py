# Exercicio 52

# 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))
count = 0

for c in range(1, numero +1):
    if numero % c == 0:
        count += 1

if count == 2:
    print('PRIMO')
else:
    print('NÃO É PRIMO')


'''for p in range(1, numero +1):
    divisao = numero / p
    if divisao.is_integer():
        if not (divisao == 1 or divisao == numero):
            count += 1

if count > 0:
    print(f'O número {numero} nao é PRIMO!')
else:
    print(f'é um número PRIMO!')'''







