#Programa que mostra a tabuada de vário números
#Um de cada vez,para cada valor digitado pelo usuário
#O programa será interrompido quando o número solícitado for negativo
n = 0
cont = 0
while True:
    n =int(input('Qual a tabuada desejada? '))
    print('-'*20)
    print(f'A tabuada de {n}:')
    print('-' * 20)
    if n <0 :
        break
    print(f' {n} x 0 = 0')
    for tabuada in range(n,n*10+n,n):
        cont+=1
        print(f' {n} x {cont} = {tabuada}')
print('-' * 20)
print('Programa tabuada encerrado. Volte sempre!')
print('-' * 20)
