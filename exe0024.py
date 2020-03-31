#programa que lê o nome de uma cidade e diz se ela começa não com o nome santo
cidade=str(input('Digte o nome da cidade: '))
divide=cidade.split()
percorre= 'Santo'in divide[0]
print('A cidade {} começa com ou não com o nome Santo? '.format(cidade),percorre)

#print(cidade[:5] == 'Santo')
