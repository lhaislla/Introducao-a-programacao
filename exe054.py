#Programa para saber se a pessoa já atingiu a maior idade ou não
from datetime import date
total_maior = 0
total_menor = 0
for pessoa in range (0,7):
    ano_nascimento = int(input('\033[3;36;mDigite o ano de seu nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if  idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print('{} pessoas já atingiram a maior idade '.format(total_maior))
print('{} pessoas ainda não atingiram a maior idade '.format(total_menor))
