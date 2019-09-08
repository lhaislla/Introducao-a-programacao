matriz = [[0,0],[0,0]]
for linha in range(0,2):
    for coluna in range(0,2):
        matriz[linha][coluna] = int(input(f'Digite um valor para {[linha]}{[coluna]}: '))
for linha in range(0,2):
    for coluna in range(0,2):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
