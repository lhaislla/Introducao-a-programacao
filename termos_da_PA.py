# Programa que lê primeiro termo e a razão de uma P.A.
# E no final mostra os 10 primeiros termos dessa progressão
#P.A: an = a1+(n-1).r
a=int(input('Digite o primeiro termo: '))
r= int(input('Digite a razão da Progressão aritmetica: '))
cont= 0
print(razao)
for c in range(a,a+10*r,r):
    cont += razao
    print('Os 10 primeiros termos dessa P.A são: {} '.format(c))
