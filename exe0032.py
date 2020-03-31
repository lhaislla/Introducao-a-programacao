#faça um  programa que leia um ano qualquer e mostre se é bissexto
from datetime import date
ano = int(input('\033[1;;41mQual ano você está? Coloque 0 para analisar o ano atual:  '))
print('\033[1;;41m-*-' * 20)
if ano ==0:
    ano = date.today().year
#Pega a data do ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[1;;41mO ano: {} é bissexto'.format(ano))
else:
     print('\033[1;;41mO ano: {} não é bissexto'.format(ano))
print('\033[1;;41m-*-' * 20)