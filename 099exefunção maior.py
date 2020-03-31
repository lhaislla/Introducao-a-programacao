#Função maior()
# Recebe varios parametros com valores inteiros
# O programa analisa todos os valores e diz qual deles é o maior
def lin ():
    print('\033[;31;m-='*30)
def maior (*n):
    cont = maior = 0
    lin()
    print(f'\033[;32;mAnalisando os valores passados:', end=" ")
    print()
    lin()
    for valor in n:

        print(f'\033[;32;m {valor}', end = ' ')

        if cont ==0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    lin()
    print('\033[;32;m')
    print(f'\033[;32;mForam informados {cont} valores ao todo')
    print()
    lin()
    print(f'\033[;32;mO maior valor informado foi: {maior}')
    lin()
maior(2,9,4,5,7,1,21,49,700,3 ,8 ,6)