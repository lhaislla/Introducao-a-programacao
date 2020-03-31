# Programa que tem uma lista camada numeros  e duas funções
# Função  sorteia () e somaPar()
# A primeira função sorteia 5 números e coloca em uma lista
# A Segunda função mostra a soma  entre todos os valores Pares
from random import randint

def sortear(lista):
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
numeros = list()
sortear(numeros)
print(numeros)
somaPar(numeros )