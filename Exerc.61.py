# Exercicio 61

# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

numero = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = numero
count = 1

while count <= 10:
    print(f'{termo} -> ', end ='')
    termo += razao
    count += 1
print('FIM')




