# Exercicio 68

#068: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0

while True:
    jogador = int(input('Diga um valor: '))
    escolha = input('Você escolhe PAR OU ÍMPAR? [P/I]: '). upper().strip()
    computador = randint(1,10)
    number = computador + jogador
    print(f'Você jogou {jogador} e o computador {computador}. Total de {number} ', end = '')
    print(f'Deu PAR' if number % 2 == 0 else 'Deu IMPAR')
    if escolha == 'P':
        if number % 2 == 0:
            print(f'Jogador ganhou!!! ')
            v += 1
        else:
            print(f'Computador ganhou!!!')
            break
    elif escolha == 'I':
        if number % 2 == 1:
            print(f'Jogador ganhou!!!')
            v += 1
        else: 
            print(f'Computador ganhou!!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')







