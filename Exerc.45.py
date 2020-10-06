#Exercicio 45

#Crie um programa que faça o computador jogar Jokenpô com você.

import random

print('Vamos jogar JOKENPÔ!!!')
print('PEDRA, PAPEL OU TESOURA')

print(' ')

print('''O que você escolhe? 
[1] Pedra
[2] Papel
[3] Tesoura
...''')

jogador = int(input('Qual a sua opção? '))
computador = random.randint(1, 3)

if jogador == 1: 
    print(f'O jogador escolheu Pedra')
elif jogador == 2:
    print(f'O jogador escolheu Papel')
else:
    print(f'O jogador escolheu Tesoura')

if computador == 1: 
    print(f'O computador escolheu Pedra')
elif computador == 2:
    print(f'O computador escolheu Papel')
else:
    print(f'O computador escolheu Tesoura')

if jogador == 1 and computador == 2:
    print(f'O computador venceu!!!')
elif jogador == 2 and computador == 1:
    print(f'O jogador venceu!!!')
elif jogador == 2 and computador == 3:
    print(f'O computador venceu!!!')
elif jogador == 3 and computador == 2:
    print(f'O jogador venceu!!!')
elif jogador == 1 and computador == 3:
    print(f'O jogador venceu!!!')
elif jogador == 3 and computador == 1:
    print(f'O computador venceu!!!')
else:
    print(f'Empate!!!')






