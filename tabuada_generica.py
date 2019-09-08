#Faça uma tabuada
# de um número que o usuário escolher,
# só que agora utilizando o laço for
n = int(input('\033[;31;mDigite o número que deseja obter a tabuada: '))
for c in range(0,11,):
    print('{} x {:2}= {}'.format(n,c, n*c))
