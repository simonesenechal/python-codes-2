# Exercicio 60

#060: Faça um programa que leia um número qualquer e mostre o seu fatorial.


#from math import factorial #usando biblioteca
#fat = factorial(numero)

#print(f'Fatorial de {numero} é {fat}')

numero = int(input('Digite um número: '))

fact = numero
fac = 1

while fact > 0:
    print(f'{fact}', end ='')
    print(f' x ' if fact > 1 else ' = ', end ='')
    fac *= fact
    fact -= 1
print(f'{fac}')