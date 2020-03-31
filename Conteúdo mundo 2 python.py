print('''#Estruturas de Controle
While condição de parada:
    -while True:
        if bloco:
            passo
        if vazio:
            pula
        if moeda:
            pega
        if trofeu:
            pula
            break
    pega
    
    
      ''')
#While True (loop infinito)
#break joga para fora de uma estrutura de repetição(Quebra um loop que esta acontecendo uma seuência de vezes)
#EX:
cont =1
while cont <=10:
    print(xont,' ',end='')
    cont += 1
print('Acabou')

cont =1
while True: #Faz pra sempre o programa
    print(cont,' ',end='')
    cont += 1
print('Acabou')

#Pedindo infinitas vezes (Utiizando flags)
n = 0
while n!= 999:
    n =int(input('Digite um número'))
#Caso queira impor uma quantidade de vezes a ser pedida é necessario um contador
n = cont = 0
while cont= 3:
    n =int(input('Digite um número'))
    cont += 1
#Soma com while
n = soma = 0
while n!= 999:
    n =int(input('Digite um número: '))
    soma += n
print('A soma vale: {}'.format(soma -999))
#Interroper em qualquer lugar
n = soma = 0
while True:
    n =int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
print('A soma vale: {}'.format(soma))
#fstring
#print(f'A soma vale: {soma}')#paython 3.6
#Ex: print('O %s tem %d anos.' %nome, %idade)#paython 2

#Condição de parada
resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp in 'N':
        break


