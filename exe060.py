#Crie um programa que crie um número qualquer e mostre seu fatorial
print('''from  math import factorial
n = int(input('Digite o número que deseja obter o fatorial:  '))
fat = factorial(n)
print('O fatorial de {} é {}'.format(n, fat))''')

print('''
#Versão While
n = int(input('Digite o número que deseja obter o fatorial:  '))
c = n
f = 1
while c> 0 :
    print('{}'.format(c),end= ' ')
    print(' x ' if c > 1 else ' = ',end='')
    f = f * c
    c -= 1
print('{}'.format( f))''')


#versão for
f=n=int(input('Informe um número: '))
for c in range(n-1,1,-1):
 f*=c
print('O fatorial de {} é {}'.format(n,f))
