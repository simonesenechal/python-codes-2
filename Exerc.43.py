#Exercicio 43

#043:Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
# de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida


peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)

print(f'O IMC é {imc:.2f}')

if imc < 18.5:
    print(f'Você está ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print(f'Você está no PESO IDEAL')
elif imc >= 25 and imc < 30:
    print(f'Você está com SOBREPESO')
elif imc >= 30 and imc < 40:
    print(f'Você está com OBESIDADE')
else:
    print(f'Você está com OBESIDADE MÓRBIDA')

    

