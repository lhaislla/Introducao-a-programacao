#Programa que joga par ou ímpar com o computador
#O jo só é interrompido se o jogador perder
#Mostra o total de vitórias consecutivas que ele conquistou ao final do jogo
import random
empate = 0
vit = 0
while True:
    n = int(input('Digite um número: '))
    computador = random.randint(0, 10)
    print('Vamos jogar par ou ímpar?  ')
    print(f'Você jogou: {n} e o computador jogou: {computador}')
    if n % 2 == 0:
        if computador % 2 == 0:
            empate +=1
            print('Empate,ambos os valores são par! ')
        elif computador % 2 !=0:
            vit += 1
            print('Você venceu! ')
    elif computador % 2 == 0:
        if n % 2 == 0:
            empate += 1
            print('Empate,ambos os valores são par! ')
        elif n % 2 !=0:
            print('O computador venceu! ')
            break
            print('O jogo acabou!')

    elif computador % 2 != 0:
        if n % 2 == 0:
            vit += 1
            print('Você venceu! ')
        elif n % 2 !=0:
            empate += 1
            print('Empate,ambos os valores são ímpar! ')

print(f'O tótal de vitórias consecutivas foi: {vit} e de empates: {empate}')

