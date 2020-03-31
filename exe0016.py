# Modulos
# incluir alguma coisa import alguma coisa(imposta todas as coisas da biblioteca especificada
# from coisa import o que eu quero(importa só o que eu quero e expecifiquei)
# exemplo:
# from math import sqrt
#import math
#import random

# ceil: faz erredondamento pra cima
# floor: arredondamento pra baixo
# trunc :truncar, conta só os valores antes da virgula
# pow:potecia
# sqrt: raiz quadrada
# factorial: calculo de fatorial
# Gera números aleatórios entre zero e um
# se quiser o random expecifico tem que especificar o tipo
#num = random.random()
#print(num)
#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
import math
n= float(input('Digite um valor: '))
arredondar= math.trunc(n)
print("Valor inteiro de {} é {}".format(n,arredondar))