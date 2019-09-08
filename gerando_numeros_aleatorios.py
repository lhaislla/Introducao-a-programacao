# Programa que gera numeros aleatórios e coloca em uma tupla
# Mostra a listagem dos números gerados
# Indica o menor e o maior valor que estão na tupla

import random


sorteio = (random.randint(0, 10),random.randint(0, 10),random.randint(0, 10),random.randint(0, 10),random.randint(0, 10))
print(f'Valores sorteados:', end = ' ')
for n in sorteio:
    print(f'{n}',end = ' ')
print(' ')
print(f'Menor valor: {min(sorteio)}')
print(f'Maior valor: {max(sorteio)}')
