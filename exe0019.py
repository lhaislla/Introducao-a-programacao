#Um professor quer sortar um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,lendo o nome deles e escrevendo o nome do escolhido.
#Sorteando um item na lista(random.choice(lista)
import random
primeiro_aluno =input('Digite o nome do aluno: ')
segundo_aluno =input('Digite o nome do aluno: ')
terceiro_aluno =input('Digite o nome do aluno: ')
quarto_aluno =input('Digite o nome do aluno: ')
lista= [primeiro_aluno,segundo_aluno,terceiro_aluno,quarto_aluno,]
sorteio = random.choice(lista)
print("O aluno sorteado foi: {}".format(sorteio))
