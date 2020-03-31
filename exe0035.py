#Programa que lê o comprimento de três retaas
#Diz a usuáriose as retas podem ou não formar um triângulo

r1 = float(input('Digite o valor da 1° reta: '))
r2 = float(input('Digite o valor da 2° reta: '))
r3 = float(input('Digite o valor da 3° reta: '))
print('-*-' * 10)
print('Analisador de Triângulos')
print('-*-' * 10)

if r1< r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podem formar um triângulo')
else:
    print('Não podem formar um triângulo')

#if (r2-r3 )< r1 < (r2 + r3):
#    print('Podem formar um triângulo')
#elif(r1-r3 )< r2 < (r1+ r3):
#    print('Podem formar um triângulo')
#elif (r1 - r2) < r3 < (r1 + r2):
#    print('Podem formar um triângulo')
#else:
#    print('Não podem formar um triângulo')
