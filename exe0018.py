#Faça um programa que lê um angulo qualquer e mostra na tela o valor do seno, cosseno e tangente

import math
angulo=float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("Seno de {}: {:.2f}".format(angulo,seno))
print("Cosseno de {}: {:.2f}".format(angulo,cosseno))
print("Tangente de {}: {:.2f}".format(angulo,tangente))