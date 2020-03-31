#programa de sorteio da ordem de apresentação de trabalhos de alunos.Lê quatro nomes e mostra a ordem sorteada
#Sorteandoem ordem os  itens da lista random.shuffle(lista)
import random
primeiro_aluno =input('Digite o nome do aluno: ')
segundo_aluno =input('Digite o nome do aluno: ')
terceiro_aluno =input('Digite o nome do aluno: ')
quarto_aluno =input('Digite o nome do aluno: ')
lista= [primeiro_aluno,segundo_aluno,terceiro_aluno,quarto_aluno,]
random.shuffle(lista)


print("a ordem  dos alunos sorteados:")
print(lista)