#Programa que lê 7 valores e cadastra em uma lista única
#Mantendo os valores separados empares e imparare
#Mostrar os valores pares de impares em ordem crescente
num = [[], []]
for i in range(0,6):
    valor = int(input('Digite o valor: '))
    if valor % 2==0:
        par =num[0].append(valor)
    else:
        impar =num[1].append(valor)
print(num)
