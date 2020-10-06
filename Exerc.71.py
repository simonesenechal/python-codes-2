# Exercicio 71

#071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('-' * 40 )
print('CAIXA ELETRÔNICO')
print('-' * 40 )

saque = int(input('Qual valor deseja sacar? '))
total = saque
cédula = 50
total_cédula = 0

while True:
    if total >= cédula:
        total -= cédula
        total_cédula += 1
    else:
        if total_cédula > 0:
            print(f'Total de {total_cédula} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        total_cédula = 0
        if total == 0:
            break


from math import floor


notas_banco = [1, 10, 20, 50]
notas_banco = sorted(notas_banco, reverse = True)

valor_saque = int(input('Valor: R$ '))

while True:
    for nota in notas_banco:
        n = valor_saque / nota
        valor_saque = valor_saque % nota
        if int(n) != 0:
            if floor(n) == 1:
                print(f'{floor(n)} nota de R${nota:.2f}')
            else:
                print(f'{floor(n)} notas de R${nota:.2f}')
        if valor_saque == 0:
                break

