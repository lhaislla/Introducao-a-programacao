#Programa que lê a idade e o sexo
#A Cada pessoa cadastrada  ele pergunta se o usuário quer continuar ou não
#Ao final mostra quantas pessoas  tem mais de 18 anos
#Quantos homens foram cadastrados
#Quantas mulheres te menos de 20 anos

maior = 0
h = 0
m20 = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] '))
    print('-' * 20)
    if idade > 18:
        maior +=1
    if sexo  in 'Mm':
        h+=1
    if sexo in 'Ff' and idade > 20:
        m20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp in 'N':
        break
print(f'Pessoas com mais de 18 anos {maior}')
print(f'A quantidae de homens cadastrados: {h}')
print(f'A quantidade de mulheres com mais de 20 anos: {m20}')
