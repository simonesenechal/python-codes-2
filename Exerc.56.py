# Exercicio 56

# 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma = 0
old = 0
nome_old = ''
total_mulheres = 0

for programa in range(1,5):
    print(f'{programa} pessoa: ')
    nome = input('Qual o seu nome? ').strip()
    idade = int(input('Qual a sua idade? '))
    sexo = input('Qual o seu sexo? [M/F]').strip()

    soma += idade
    age = soma / 4

    if programa == 1 and sexo in 'Mm':
        old = idade
        nome_old = nome
    if sexo in 'Mm' and idade > old:
        old = idade
        nome_old = nome
    if sexo in 'Ff' and idade < 20:
        total_mulheres += 1

print(f'A média de idades do grupo é {age}.')
print(f'O homem mais velho é {nome_old} e ele tem {old} idade.')
print(f'O total de mulheres com menos de 20 anos é {total_mulheres}.')
















