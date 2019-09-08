#Programa ppara saber o maior e o menor peso
maior = 0
menor = 0
for pe in range (0,5):
    peso = int(input('\033[3;36;mQual o seu peso?  '))

    if  peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('Maior peso: {}  '.format(maior))
print('Menor peso: {} '.format(menor))
