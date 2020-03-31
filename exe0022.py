#Exercicío
#Programa que Lê o nome completo de uma pessoa  emostra com todas as letras minúscilas;mostra todas  as maiusculas e  quantas letras tem ao nome(sem considerar espaços) e quantas letras tem o primeiro nome,
nome=str(input('\033[1;;41mdigite seu nome completo: ')).title()
letras_sem_espaco = nome.strip()
tamanho_sem_espaco = len(letras_sem_espaco)-nome.count(' ')
separando = nome.split()
dividido = separando[0]
print('\033[1;;41m {}'.format(nome))
print('\033[1;;41mnome em maiúsculo:', nome.upper())
print('\033[1;;41mnome em minúsculo:', nome.lower())
print('\033[1;;41mTamanho da frase sem espaços:  ', tamanho_sem_espaco)
print('\033[1;;41mQuantidade de  letras do primeiro nome: ',len(dividido))
#print('Tamanho da frase: ',  len(nome) )
#pra quantas letras tem no primeiro nome poderia ter usado nome.find('')

