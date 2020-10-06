# Exercicio 62

#062: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

numero = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = numero
count = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while count <= total:
        print(f'{termo} -> ', end ='')
        termo += razao
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos você gostaria a mais? '))
print(f'Progressão finalizada com {total} termos gerados.')




