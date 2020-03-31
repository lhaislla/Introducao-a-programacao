#Programa que calcula a soma entre todos os números ímpares
#Multiplos de três
#Que se encontram no intervalo de 1 a 500

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c% 3==0:
        cont = cont + 1
        soma = soma + c
    print('O somatório de todos os {} valores foi: {} '.format(cont,soma))