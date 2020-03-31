#Programa que lê  nome e duas notas d evário alunos
#Guarda  tudo em uma lista composta
# Mostra o boletom no final contendo média de cada um dos alunos  e as notas de cada aluno individualmente

ficha = list()
while True:
    nome = str(input('NOme: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2 ) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Que continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÈDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interromper)'))
    if opc == 999:
        print('FINALIZANDO')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {cad[opc][1]}')
print('<<< VOLTE SEMPRE >>>')