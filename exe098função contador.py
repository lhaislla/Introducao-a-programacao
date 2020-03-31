# Função contador()
# Recebe trê paramêtros: inicio, sim e passo  e realiza a contagem
# O programa realiza três contagens através da função criada
#   a) de 1 até 10, de 1 em 1
#   b) De 10 até 0, de 2 em 2
#   c) Uma contagem personalizada( 7 em 7 )
#flush = False é uma particularidade ddo sleep ( ele faz com que o buff de tela não seja ligado)
from time import sleep
def lin():
    print('\033[;35;m-=-' * 40)
def contagem(inicio,fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2.5)
    if passo < 0:
        p *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = 1
        while cont <=fim:
            print(f'{cont}', end = " ",flush = False)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = 1
        while cont >= fim:
            print(f'{cont}', end = ' ', flush = False)
            sleep(0.5)
            cont -= passo
        print(' FIM!')
        lin()
contagem(1,10,1)
contagem(inicio =10,fim=0,passo=2)
lin()
print('Agora é sua vez de personalizar a contagem')
lin()
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contagem (i,f,p)