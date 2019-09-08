# Matriz  de dimensão 3x3
# Preenche com valores lidos pelo teclado
# Soma de todos os valores pares
# Soma dos valores da terceira coluna
# O maior vlor da segunda coluna
matriz = [[0,0,0], [0,0,0], [0,0,0]]
#For para colocar os valores dentro da matriz
for linha in range(0,3):
    for coluna in  range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {[linha ]}{[coluna]}: '))
#For para dar o formato de matriz
for linha in range (0,3):
    for coluna in range (0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end ='')
    print()
somapar = 0
somacoluna =0
maior = 0
if matriz[linha][coluna] % 2== 0:
    somapar += matriz[linha][coluna]
    print(f'A soma dos valores pares é{somapar}')
for linha in range(0,3):
    somacoluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {somacoluna}')
for coluna in range(0,3):
    if coluna ==0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna]> maior:
        maior = matriz[1][coluna]

print(f'O maior valor da segunda linha é {maior}')
