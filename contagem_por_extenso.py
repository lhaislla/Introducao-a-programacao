#Programa que cria uma tupla totalmente preenchida
#de 0 a 20
#ler um número de 0 a 20
#mostra por extenso

extenso = ('Zero','Um', 'Dois', 'Três', 'Quatro','Cinco', 'Seis','Sete','Oito','Nove', 'Dez', 'Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezesete','Dezoio','Dezenove','Vinte')
while True:
    numero = int(input('\033[;36;mDigite um número de 0 a 20: '))
    if  0 <  numero <= 20:
        break
    print('Tente novamente.',end = '')
print (f'\033[;32;mVocê digitou o número: {extenso[numero]}')


