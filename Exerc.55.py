# Exercicio 55

# 055: Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for peso in range(1, 6):
    pessoa = float(input(f'Qual o peso da {peso}ª pessoa? '))
    if peso == 1:
        maior = pessoa
        menor = pessoa
    else: 
        if pessoa > maior:
            maior = pessoa
        if pessoa < menor:
            menor = pessoa
    
print(f'O maior peso é {maior}kg e o menor peso é {menor}kg.')



