#Programa que lê o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa
import  math
cateto_oposto=float(input('Digite o valor do cateto oposto: '))
cateto_adjacente=float(input('Digite o valor do cateto adjacente: '))
hipotenusa=math.sqrt((cateto_oposto)**2+ (cateto_adjacente)**2)
print("O Cumprimento da Hipotenusa é de : {:.2f}".format(hipotenusa))