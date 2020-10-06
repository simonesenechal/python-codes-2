# Resolução Guanabara

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)


# Resolução Thulio

opcoes = {1: 'Pedra',
2: 'Papel',
3: 'Tesoura'}

jogador = int(input('Digite sua opcao: '))

opcao_jogador = opcoes.get(jogador, 'Valor não permitido')

print(opcao_jogador)

