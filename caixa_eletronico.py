#Programa que simula o funcinamento de um caixa eletrônico
#Pergunte o valor a ser sacado
#Programa informa quantas cedulas de cada valor serão entregues
# Cada caixa possui cédulas de R$50, R$20, R$10 e R$1.

cont = 0
print('-' * 20)
print('        Banco    ')
print('-' * 20)
valor = int(input('Qual valor a ser sacado? '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced :
        total -= ced
        totalced += 1
    else:
        if totalced >0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced  == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('-' * 20)
print('Volte sempre ao banco! ')






