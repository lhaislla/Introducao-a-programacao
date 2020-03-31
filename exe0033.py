#Programa que lê três números
#Mostra qual é o maior número entre eles
#Mostra qual é o menor número entre eles

n1 = int(input('\033[1;;41mDigite o 1° valor: '))
n2 = int(input('\033[1;;41mDigite o 2° valor: '))
n3 = int(input('\033[1;;41mDigite o 3° valor: '))
print('\033[1;;41m-*-' * 20)

if (n1 > n2) and (n1 >  n3):
    print('\033[1;;41mO número {} é o maior valor'.format(n1))
    if n2 > n3:
        print('\033[1;;41mo número {} é o menor valor'.format(n3))
    else:
        print('\033[1;;41mo número {} é o menor valor'.format(n2))
elif (n2 > n1) and (n2 >  n3):
    print('\033[1;;41mO número {} é o maior valor'.format(n2))
    if n1 > n3:
        print('\033[1;;41mo número {} é o menor valor'.format(n3))
    else:
        print('\033[1;;41mo número {} é o menor valor'.format(n1))
else:
     print('\033[1;;41mO número {} é o maior valor'.format(n3))
     if n1 > n2:
         print('\033[1;;41mo número {} é o menor valor'.format(n2))
     else:
         print('\033[1;;41mo número {} é o menor valor'.format(n1))
print('\033[1;;41m-*-' * 20)
#Outro jeito:
#print('''
#a= int(input('primeiro valor: )
#b= int(input('segundo valor: )
#c= int(input('terceio valor: )
#if a<b and a<c:
#    menor = a
#if b<c and b<a:
#    menor = b
#if c<a and c <b:
#    menor = c
#''')
#print('''
#Verificando quem é o menor
#a= int(input('primeiro valor: )
#b= int(input('segundo valor: )
#c= int(input('terceio valor: )
#menor = a
#if b<a and b<c:
#    menor = a
#if c<a and c <b:
#    menor = c
#verificando quem é o maior
# maior = a
#if b>a and b>c:
#   maior = b
#if  c>a and c>b:
#   maior = c
#''')