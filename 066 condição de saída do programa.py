#Programa que lê varios números inteiros no teclado
#O programa só para quando o usuário digitar 999
#Mostra a quantidade de números digitados
#Mostra a soma entre eles, desconsiderando o flag
n = soma = cont = 0
while True:
    n =int(input('\033[;32;mDigite um número(999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos  {cont} valores foi: {soma}')