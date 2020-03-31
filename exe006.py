#Programa que lê um número e mostra o seu dobro,triplo e raiz quadrada
import math
n=int(input("Digite um número: "))
dobro = 2*n
triplo= 3*n
#r = n **(1/2)
raizq=math.sqrt(n)
print("\033[5;36;41mResultados: dobro = {} ,triplo = {}  , raiz quadrada = {" "}  ".format(dobro,triplo,raizq))