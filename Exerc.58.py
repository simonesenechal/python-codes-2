# Exercicio 58

#58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

import random

print(f'Descubra qual o número escolhido entre 0 e 10.')

count = 1
computador = random.randint(0,10)
jogador = int(input('Qual o seu palpite? '))

while jogador != computador:
    count += 1
    if jogador < computador:
        print(f'Você errou, o número é maior, tente novamente!')
        jogador = int(input(f'Escolha outra opção: '))
    else:
        print(f'Você errou, o número é menor, tente novamente!')
        jogador = int(input(f'Escolha outra opção: '))

print(f'Parabéns você acertou! O computador também escolheu o número {computador}')  
print(f'Acertou em {count} tentativas!')









