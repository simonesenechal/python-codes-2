# Exercicio 53

# 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços. 

frase = input('Digite uma frase: ').strip().upper()
word = frase.split()
junto = ''.join(word)
inverso = junto[::-1] #fatiamento
'''inverso = '''''

'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''

print(f'O inverso de {junto} é {inverso}.')

if inverso == junto:
    print(f'Temos um palíndromo!')
else:
    print(f'A frase digitada não é um palíndromo!')
 

# Outra opção sem o for




