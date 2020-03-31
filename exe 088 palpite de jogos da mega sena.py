# Programa que cria palpites
# Pergunta quantos jogos serão gerados
# Sorteia 6 números entre 1 e 60
# CAdastra cada jogo em uma lista composta

from  random import randint
lista =list()
jogos = list()
print('-' * 30)
print('     JOGA NA MEGA SENA       ')
print('-' * 30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <=  quantidade:
    cont = 0
    while True:
        num =randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont+= 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'Os números sorteados foram: {jogos}')
print('-=' *3 , f'SORTEANDO {quantidade} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')