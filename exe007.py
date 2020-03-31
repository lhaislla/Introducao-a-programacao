#Programa que lê duas notas de um aluno,calcula e mostra sua média

nota1=float(input('\033[3;;41mDigite a nota da 1° avaliação: '))
nota2=float(input('\033[3;;41mDigite a nota da 2° avaliação: '))
media= (nota1 + nota2)/ 2
print('\033[;;41mMédia: {}'.format(media))