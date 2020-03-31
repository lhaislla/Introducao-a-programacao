# Matriz  de dimensão 3x3
# Preenche com valores lidos pelo teclado
# No final mostra na tela com a formatação correta
matriz = [[0,0,0], [0,0,0], [0,0,0]]
#For para colocar os valores dentro da matriz
for linha in range(0,3):
    for coluna in  range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor: '))
#For para dar o formato de matriz
for linha in range (0,3):
    for coluna in range (0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end ='')
    print()