# Exercicio 69

# 069: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

print('-' * 30)
print('CADASTRE UMA PESSOA')
print('-' * 30)

ask = 'S'
count = count1 = count2 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = input('Sexo [F/M]: ').strip().upper()
        print('-' * 30)
    if idade >= 18:
        count += 1
    if sexo == 'M':
        count1 += 1
    if sexo == 'F' and idade < 20:
        count2 += 1
    ask = ' '
    while ask not in 'SN':
        ask = input('Deseja continuar? [S/N]: ').strip().upper()
    if ask == 'N':
        break
print(f'{count} pessoas são maiores de 18 anos, existe {count1} homens cadastrados e {count2} mulheres com menos de 20 anos.')







