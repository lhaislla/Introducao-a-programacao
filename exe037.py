#Programa que lê um número inteiro qualquer
#Pede para um usuário escolher qual a base de conver são
#- 1 para binário
#- 2 para octal
#- 3 para hexadecimal

n = int(input('\033[1;31;mDigite um número inteiro:  '))
converter =int(input('''\033[1;31;mQual a base de conversão que você deseja escolher?
Digite:
- 1 para binário
- 2 para octal
- 3 para hexadecimal 
Escolha: '''))
if converter == 1:
    binario = bin(n)
    print('\033[1;33;mO número {} em binário é: {}'.format(n, binario[2:1]))
elif converter == 2:
    octal = oct(n)
    print('\033[1;33;mO número {} em octal é: {}'.format(n, octal[2:] ))
elif converter == 3:
    hexadecimal = hex(n)
    print('\033[1;33;mO número {} em hexadecimal é: {}'.format(n, hexadecimal[2:]))
else:
    print('''\033[1;33;mOpção de escolha indisponivel! ''')
