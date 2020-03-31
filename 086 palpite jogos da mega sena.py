# Programa que cria palpites
# Pergunta quantos jogos serão gerados
# Sorteia 6 números entre 1 e 60
# CAdastra cada jogo em uma lista composta

from  random import randint
lista =list()
jogos = list()
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 0
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
print(f'Os números sorteados foram {jogos}')