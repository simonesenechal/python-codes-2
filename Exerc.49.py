# Exercicio 49

#049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, 
# só que agora utilizando um laço for.

numero = int(input('Digite um número: '))

for c in range(0,11):
    tabuada = numero * c
    print(f'{numero} x {c} = {tabuada}')


# Tabuada completa

'''for i in range(1, 11):
    print('\n====================')
    print(f'   Tabuada do {i}:')
    print('====================\n')

    for j in range(11):
        print(f'{i} x {j} = {i*j}')'''






