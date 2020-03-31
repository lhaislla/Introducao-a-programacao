#Programa que  mostra na tea uma contagem
# regressiva para o astouro de fogos de artificio,indo de 10 até 0,
# com uma pausa de 1 segundo entre eles
from time import sleep
for c in range(10, -1, -1):
    print('Contagem regressiva para o estouro de fogos de atifícios:{}'.format(c))
    sleep(0.5)
print('FIM')