# Exercicio 67

#067: Faça um programa que mostre a tabuada de vários números, um de cada vez, 
# para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.


while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num <= 0:
        break
    for tabuada in range(0,11):
        multi = num * tabuada
        print(f'{num} x {tabuada} = {multi}')
print('FIM')





