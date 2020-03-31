#Programa que diz se é um número primo
n =int(input('\033[;31;mDigite um número: '))
total =0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[33m',end=' ')
        total+=1
    else:
        print('\033[31m',end=' ')
    print('{}'.format(c),end=' ')
print('o número {} foi divisivel {} vezes'.format(n,total),end=' ')
if total == 2:
    print('É PRIMO! ')
else:
    print(('NÃO É PRIMO! '))