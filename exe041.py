#Programa que lê o ano de nascimento do atleta e mostra sua categoria de acordo com a idade
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JUNIOR
#- Até 20 anos: SÊNIOR
#- ACIMA: MASTER

from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('\033[3;36;mDigite o ano de seu nascimento: '))
idade = ano_atual - ano_nascimento
print('O Atleta tem: {} Anos'.format(idade))
if idade <= 9:
    print('\033[1;31;mCategoria: MIRIM')
elif idade >= 9 and idade <=14:
    print('\033[1;31;mCategoria: INFANTIL')
elif idade >= 14 and idade <=19:
    print('\033[1;31;mCategoria: JUNIOR')
elif idade >= 20:
    print('\033[1;31;mCategoria: SÊNIOR ')
