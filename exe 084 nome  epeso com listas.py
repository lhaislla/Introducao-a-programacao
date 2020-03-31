# Programa que lê o nome e peso de várias pessoas
# Mostra quantas pessoas foram castradas
# Mostra uma listagem com pessoas mais pesadas
# Um listagem com as pessoas mais leves

temp = list()
princ = list()
maior = 0
menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    r = str(input('Deseja continuar? [S/N] ')).upper()
    if len(princ)==0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    if r == 'N':
        break
print(f'Os dados foram: {princ}')
print(f'Total de cadastros: {len(princ)}')
print(f'O maior peso foi {maior} Kg ')
print(f'O menor peso foi {menor} Kg ')