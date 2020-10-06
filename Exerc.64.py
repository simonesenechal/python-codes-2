# Exercicio 64

#064: Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = 0
num = int(input('Digite um número ou [999] para parar: '))
count = 0
limite = 999
soma = 0

while num != limite:
    count += 1
    soma += num
    num = int(input('Digite um número ou [999] para parar: '))
print(f'Você digitou um total de {count} números e a soma entre eles é {soma}')

