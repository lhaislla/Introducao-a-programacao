#Programa quelÊ dois números inteiros e compara-os mostrando na tela uma mensagem
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior os dois são iguais
n1 = float(input('\033[1;31;mDigite o primeiro número: '))
n2 = float(input('\033[1;31;mDigite o segundo número: '))

if n1 > n2:
    print('\033[1;35;mO primeiro valor é maior')
elif n2 > n1:
    print('\033[1;32;mO segundo valor é maior')
else:
    print('\033[1;34;mNão existe valor maior os dois são iguais')