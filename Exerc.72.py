# Exercicio 72

# 072: Crie um programa que tenha uma tupla totalmente preenchida 
# com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# O programa vai perguntar se ele deseja continuar.

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 
'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 
'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    if 0 <= escolha <= 20:
        print(f'Você digitou o número {numeros[escolha]}')
        escolha1 = input('Deseja continuar [S/N]: ').strip().upper()
        if escolha1 == 'N':
            break
    elif escolha > 20:
        print(f'Número incorreto.', end = ' ')
print('Obrigada!')



