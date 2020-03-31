# programa que le 5  números aletórios
# Coloca em uma tupla
# Mostra a listagem dos números gerados
# Mostra o menor e maior valor que estão na tupla

import random

sorteio=(random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))
print('Valores sorteados:', end= ' ')
print(f'{sorteio}')
print(' ')
print(f'Maior valor sorteado: {max(sorteio)}')
print(f'Menor valor sorteado: {min(sorteio)}')
