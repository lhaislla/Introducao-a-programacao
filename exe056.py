#Programa
somaidade = 0
maior = 0
nomevelho = ''
cont = 0
for i in range(1,5):
    print(i)
    nome = str(input('\033[;36;mQual seu nome? '))
    idade = int(input('\033[;32;mQual sua idade? '))
    sexo = str(input('''\033[;31;m
    Digite:
           F- Feminino
           M- Masculino
    Qual seu sexo:  ''')).upper()
    somaidade +=idade
    media = somaidade/4

    if i == 1 and sexo in 'Mm':
        maior = idade
        nomevelho = nome
    if sexo in 'Mm'and idade > maior:
        maior = idade
        nomevelho = nome
    if sexo in'Ff' and idade < 20:
        cont += 1
print('media de idade do grupo: {:.2f}'.format(media))
print('Mulheres com menos de 20 ano : {}'.format(cont))
print('Homem mais velho tem {} anos e se chama: {}  '.format(maior,nomevelho))




