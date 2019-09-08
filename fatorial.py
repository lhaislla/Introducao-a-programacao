n =int(input('Digite o número que deseja obter o fatorial: '))
c = n
#Fatorial com While
while c >0:
    print('{} x'.format(c),end = '')
    c -=1
    f *= c
print('O fatorial de {}[e {}'.format(n,f))

#Fatorial com for
f=n =int(input('Digite o número que deseja obter o fatorial: '))
for c in range(n-1,1,-1):
    f*=c
print (' {}! = {}'.format(n,f))
