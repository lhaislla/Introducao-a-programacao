#Programa que lê dois valores e mostra um menu na tela
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
#O programa deverá realizar a operação solicitada em caso

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('\033[;31;m-==-'*10)
print('''\033[;31;m
    \033[;32;m[1] somar
    \033[;32;m[2] multiplicar
    \033[;32;m[3] maior
    \033[;32;m[4] novos números
    \033[;32;m[5] sair do programa
''')
print('\033[;31;m-==-'*10)
escolha = 0
while escolha != 5:
    escolha = int(input('\033[;32;mOpção de escolha: '))
    if escolha == 1:
        soma = n1 + n2
        print('Resultado da soma de {} + {} = {}'.format(n1,n2,soma))
        print('\033[;31;m-==-' * 10)
    elif escolha == 2:
        mult = n1 * n2
        print('Resultado da multiplicação de {} x {} = {}'.format(n1, n2, mult))
        print('\033[;31;m-==-' * 10)
    elif escolha == 3 :
        if n1 > n2:
            maior = n1
            print('Maior valor: {}'.format(maior))
            print('\033[;31;m-==-' * 10)
        else:
            maior = n2
            print('Maior valor: {}'.format(n2))
            print('\033[;31;m-==-' * 10)
        print('\033[;322;mEntre {} e {} o maior valor é '.format(n1,n2,maior))
    elif escolha == 4:
        print('insira novos valores')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print('\033[;31;m-==-' * 10)

    elif escolha == 5 :
        print('Saindo do programa')
        print('\033[;31;m-==-' * 10)
    else:
        print('Opção invalida')
        print('\033[;31;m-==-' * 10)
print('Fim do programa!')
print('\033[;31;m-==-'*10)




