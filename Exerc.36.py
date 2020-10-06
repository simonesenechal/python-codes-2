#Exercicio 36

#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

house = float(input('Qual o valor da casa que você deseja? '))
salary = float(input('Qual o valor do seu salário? '))
year = float(input('Em quantos anos deseja pagar? '))
meses = year * 12.0
parcela = house / meses
limite = salary * 0.3

print(f'Com um salário de R${salary:.2f} e o valor da casa R${house:.2f} \
sua parcela fica no valor R${parcela:.2f}.')
print(f'O valor máximo para a parcela é de R${limite:.2f}')

if parcela <= limite:
    print(f'Seu empréstimo foi APROVADO!')
elif parcela >= limite:
    print(f'Seu empréstimo foi NEGADO!')

















