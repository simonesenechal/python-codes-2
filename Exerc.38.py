#Exercicio 38

#038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 < num2:
    print(f'O segundo número é o maior')
elif num1 > num2:
    print(f'O primeiro número é maior')
else:
    print(f'O números são iguais')

