#Exercicio 39

#039: Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date


ano = int(input('Qual o ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
limite = 18
tempo = limite - idade

print(' ')

print(f'Quem nasceu em {ano} tem {idade} anos de idade em {anoatual}')

if idade < 18:
    print(f'O alistamento ainda não é obrigatório, faltam {abs(tempo)} anos.')
elif idade > 18:
    print(f'O alistamento para você é obrigatório há {abs(tempo)} anos.')
else:
    print(f'Você deverá se alistar este ano.')








