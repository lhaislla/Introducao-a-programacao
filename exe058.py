#Melhore o jodo do desafio 28, onde o computador vai pensar em um número de 0 a 10
#Só que agora o jogador vai adivinhar até acertar
#Mostrando no final quantos palpites foram necessarios para vencer

#Programa que faz o computador pensar em um número inteiro entre 0 e 5
#Usuário deve tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu

import random
#Pderia ser computador = randint(0,5)
#Print('Pensei no númer{}.format(computador))
lista= [0,1,2,3,4,5,6,7,8,9,10]
valor = False
print('\033[;31;mDigite um valor entre 0 e 10: ')
sorteio = random.choice(lista)

print('\033[;36;m-*-' * 20)
tentativas = 0
while valor != sorteio:
    valor = int(input('\033[1;36;mDigite um valor entre 0 e 10 novamente: '))
    tentativas += 1
    if sorteio == valor:
        print('\033[1;36;mParabéns você venceu! ')

    else:
        if valor < sorteio:
            print('\033[1;32;mMais... Tente mais uma vez')
        elif valor > sorteio:
            print('\033[1;32;mMenos... Tente mais uma vez')
        print('Você perdeu! ')
print('O número escolhido pelo computador foi: {}'.format(sorteio))
print('A quantidade de tentativas:{} '.format(tentativas))
print('-*-' * 20)

print('''
#outro jeito 
from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será   que você consegue adivinhar qual foi? ')
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite'))
    if jogador == computador:
        acertou = True
print('Acertou')''')
