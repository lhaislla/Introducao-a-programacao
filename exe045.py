#Crie um rpgrama que faça o computador jogar Jokenpô com você
#soteia um dos itens da lista: random.choice(lista)
import  random
lista = ['Pedra','Papel','Tesoura']
computador = random.choice(lista)
print('\033[;34;m--*--'*10)
print('''\033[;31;m
Opções de escolha:

    \033[;31;m1- Pedra
    \033[;31;m2- Papel 
    \033[;31;m3- Tesoura 
    
''')
print('\033[;34;m--*--'*10)
competidor = int(input('\033[;31;mEscolha:'))
print('\033[;34;m--*--'*10)
if competidor == 1:#Pedra
    selecao = 'Pedra'
    print('\033[;31;mO computador escolheu: {}'.format(computador))
    print('\033[;31;mVocê escolheu:{}'.format(selecao))
    if computador == 'Pedra' and selecao == 'Pedra':
        print('\033[;31;mO jogo empatou')
    elif computador == 'Tesoura' and selecao == 'Pedra':
        print('\033[;31;mVocê Venceu!')
    elif computador== 'Papel' and selecao == 'Pedra':
        print('\033[;31;mO computador venceu!')
elif competidor == 2:#Papel
    selecao = 'Papel'
    print('\033[;31;mO computador escolheu: {}'.format(computador))
    print('\033[;31;mVocê escolheu:{}'.format(selecao))
    if computador == 'Tesoura' and selecao == 'Papel':
        print('\033[;31;mComputador venceu!')
    elif computador == 'Pedra' and selecao == 'Papel':
        print('\033[;31;mVocê venceu!')
    elif computador == 'Papel' and selecao == 'Papel':
        print('\033[;31;mO jogo empatou')

elif competidor == 3:#Tesoura
    selecao = 'Tesoura'
    print('\033[;31;mO computador escolheu: {}'.format(computador))
    print('\033[;31;mVocê escolheu:{}'.format(selecao))
    if computador == 'Tesoura' and selecao == 'Tesoura':
        print('\033[;31;mO jogo empatou')
    elif computador == 'Pedra' and selecao == 'Tesoura':
        print('\033[;31;mO computador ganhou!')
    elif computador == 'Papel' and selecao == 'Tesoura':
        print('\033[;31;mVocê venceu!')
else:
    print('\033[;31;mOpção selecionada invalida!')
print('\033[;34;m--*--'*10)

print('''Outra forma de fazer:
from random import randint
itens = ('Pedra','Papel','Tesoura')
computador =randint(0,2)
print('O computador escolheu {}'.format(itens[computador]))
jogador = int(input('Qual a sua jogada? '))
print('Computador jogou{}'.format(itens[computador]))
print('jogador jogou {}.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE') 
    
    elif jogador ==1:
        print('JOGADOR VENCE')
    
    elif jogador ==2:
        print('COMPUTADOR VENCE')
    
    
    else:
        print('Jogada inválida')
        
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador ==1:
        print('EMPATE')    
    elif jogador ==2:
         print('JOGADOR VENCE')    
    else:
    print('Jogada inválida')
    
elif computador == 2:
    if jogador == 0:
         print('JOGADOR VENCE')
    elif jogador ==1:
        print('COMPUTADOR VENCE') 
    elif jogador ==2:
        print('EMPATE')
    else:
        print('Jogada inválida')

''')