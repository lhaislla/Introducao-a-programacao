#Programa que diz se o valor lido é par ou impar

valor = int(input('\033[1;;41mDigite um núemro qualquer: '))
print('-*-' * 20)
if valor % 2 == 0:
    print('\033[1;;41mO número: {} é par'.format(valor))
else:
    print('\033[1;;41mO número: {} é ímpar'.format(valor))
print('-*-' * 20)