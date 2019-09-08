lista = list()
while True:
    valor = int(input('Digite um valor:  '))
    if valor not in lista:
        lista.append(valor)
        print('Adicionado com sucesso...')
    else:
        print('Valor duplicado! não vou adicionar...')
    r = str(input('Quer continuar? [S/N] ')).upper()
    if r in 'Nn':
        break
lista.sort()
print(f'Você digitou os valores: {lista}')


