# Exercicio 57

#057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = input('Qual é o seu sexo [M/F]? ').strip().upper()

while (sexo != 'M' and sexo != 'F'):
    print(f'Opção inválida, digite novamente: ')
    sexo = input('Qual é o seu sexo [M/F]? ').strip().upper()

print(f'Ok, opção válida!')
