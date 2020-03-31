#Programa que lê seis números inteiros
#Mostra soma apenas daqueles que forem pares.
#Se o valor for ímpar ,desconsidere-o
soma = 0
cont = 0
for c in range(0, 6):
    n = (int(input('\033[;31;mDigite um número: ')))
    if n% 2==0:
        soma += n
        cont +=1
print('\033[;36;mO somatório de todos os valores pares  foi: {} '.format(soma))
