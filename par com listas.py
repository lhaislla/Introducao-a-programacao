#Programa que lê um valor
#Diz se é par ou ímpar e adiciona nas respectivas listas


lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).upper()
    if r in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'lista completa: {lista}')
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')