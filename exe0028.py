#Programa que faz o computador pensar em um número inteiro entre 0 e 5
#Usuário deve tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu

import random
#Pderia ser computador = randint(0,5)
#Print('Pensei no númer{}.format(computador))
lista= [0,1,2,3,4,5]
valor = int(input('\033[1;;41mDigite um valor entre 0 e 5: '))
sorteio = random.choice(lista)
print('\033[1;;41m-*-' * 20)

if sorteio == valor:
    print('\033[1;;41mParabéns você venceu! O número escolhido foi: {}'.format(sorteio))

else:
     print('\033[1;;41mVocê perdeu! O número escolhido foi:{}'.format(sorteio))
print('-*-' * 20)