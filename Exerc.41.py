#Exercicio 41

#041: A Confederação Nacional de Natação precisa de um programa que leia 
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: 
# - Até 9 anos: MIRIM 
# - Até 14 anos: INFANTIL 
# - Até 19 anos: JÚNIOR 
# - Até 25 anos: SÊNIOR 
# - Acima de 25 anos: MASTER

from datetime import date

ano = int(input('Qual o ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano 

print(f'A sua idade é de {idade} anos.')

if idade <= 9:
    print(f'Atleta MIRIM')
elif idade <= 14:
    print(f'Atleta INFANTIL')
elif idade <=19:
    print(f'Atleta JUNIOR')
elif idade <= 25:
    print(f'Atleta SÊNIOR')
else:
    print(f'Atleta MASTER')
    

