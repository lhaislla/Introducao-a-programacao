operacao = input()
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)
soma = 0
total = 0
for i in range(12):
    for j in range(0,11-i):
        soma += matriz[i][j]
        total +=1
if operacao=="S":
    print("%.1f" %soma)
else:
    print("%.1f" %(soma/total))

