#Programa que lê o nome completo de uma pessoa
#Mostra o primeiro e o último nome
nome = str(input('\033[1;;46mDigite seu nome completo: ')).title()
separado = nome.split()
primeiro_nome = separado[0]
quantidade = len(separado)-1
ultimo_nome = separado[quantidade]
print('\033[1;;46mSeu primeiro nome é:{} '.format(primeiro_nome))
print('\033[1;;46mSeu último nome é : {}'.format(ultimo_nome))
