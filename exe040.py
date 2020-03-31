#Programa que lê duas notas de alunos
#Calcula a média e exibe uma mensagem no final, de acordo com a média atingida
#-Média abaixo de 5.0:Reprovado
#-Média entre 5.0 e 6.9:Recuperação
#_Média 7.0 ou superior: Aprovado

n1 =float(input('\033[;36;mDigite a primeira nota:'))
n2 = float(input('\033[;36;mDigite a segunda nota:'))
media= (n1+n2)/2
if media < 5.0:
    print('\033[1;31;mREPROVADO')
elif media >= 5.0 and media <=6.9:
    print('\033[1;32;mRECUPERAÇÂO')
else:
    print('\033[1;34;mAPROVADO')