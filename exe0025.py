#Pragrma que diz se a pessoa tem Silva no nome
nome=str(input('Qual seu nome completo? ')).strip().title()
print('{} tem Silva  nome completo? '.format(nome),'Silva' in nome)