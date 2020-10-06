# Exercicio 65

# 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
soma = quant = media = maior = menor = 0

while resp == 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    media = soma / quant
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = input('Deseja continuar? [S/N]: ').upper().strip()
print(f'Você digitou {quant} números e a média é de {media:.2f}')
print(f'O maior número é {maior} e o menor {menor}')

