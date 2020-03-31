#Programa que lê nome e preço de vários produtos
#Pergunta se p usuario vai continuar
#Mostra qual o total gasto na compra
#Quantos produtos custam mais de R$ 1000
#Qual o nome do produto mais barato
total = 0
quant = 0
barato = ' '
cont = 0
menor = 0
while True:
    print('-' * 20)
    print('     COMPRE JÁ   ')
    print('-' * 20)
    produto = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o preço do produto? '))
    total += preco
    cont += 1
    if preco > 1000:
        quant +=1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp in 'N':
        break
print(f'Total gasto na compra R$ {total:.2f}')
print(f'Quantidade de produtos que custam mais de R$ 1000: {quant}')
print(f'O produto mais barato cursta: R$ {menor:.2f}')
print(f'O nome do produto mais barato é: {barato}')