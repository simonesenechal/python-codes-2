#Exercicio 42

#042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar 
# que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

reta1 = int(input('Primeiro segmento: ')) 
reta2 = int(input('Segundo segmento: '))
reta3 = int(input('Terceiro segmento: '))


if (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta1 + reta3) > reta2:
    print(f'Neste caso podemos formar um triângulo!')
    if reta1 == reta2 == reta3:
        print(f'Temos um triângulo equilátero')
    elif reta1 == reta2 != reta3 or reta2 == reta3 != reta1 or reta1 == reta3 != reta2:
        print(f'Temos um triângulo isósceles')
    else: 
        print(f'Temos um triângulo escaleno')
else:
    print(f'Neste caso não podemos formar um triângulo!')




