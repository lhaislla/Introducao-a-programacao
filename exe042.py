##Programa que lê o comprimento de três retaas
#Diz a usuáriose as retas podem ou não formar um triângulo
#Se ele puder formar um triângulo:
#-Equilátero: Todos os lado iguais
#-Isósceles: dois lados iguais
#-Escaleno: todos os lados diferentes
print('\033[;34;m-*-' * 10)
r1 = float(input('\033[;31;mDigite o valor da 1° reta: '))
r2 = float(input('\033[;31;mDigite o valor da 2° reta: '))
r3 = float(input('\033[;31;mDigite o valor da 3° reta: '))
print('\033[;34;m-*-' * 10)
print('\033[;31;mAnalisador de Triângulos:')
print('\033[;34;m-*-' * 10)

if r1< r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[;31;mPodem formar um triângulo')
    print('-*-' * 10)
    if r1== r2 == r3:
        print('\033[;31;mEquilátero: Todos os lado iguais')
        print('\033[;34;m-*-' * 10)
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('\033[;31;mIsósceles: dois lados iguais')
        print('\033[;34;m-*-' * 10)
    elif r1!= r2 and r1!=r3 and r2!= r3 :
        print('\033[;31;mEscaleno: todos os lados diferentes')
        print('\033[;34;m-*-' * 10)
else:
    print('\033[;31;mNão podem formar um triângulo')
    print('\033[;34;m-*-' * 10)

