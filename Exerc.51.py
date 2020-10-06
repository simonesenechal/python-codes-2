# Exercicio 51

# 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
n = 10

ultimo = primeiro + (n-1)*razao
ultimo += 1

for pa in range(primeiro, ultimo, razao):
    print(pa)


    

