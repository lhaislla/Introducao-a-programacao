# Programa que lê uma frase e mostra quantas vezes aparece a letra A;
# Em que posição ela aparece a  primeira vez;
# Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).title()
repeticao = frase.count('a')
posicao1 =frase.find('a')
posicao_final= frase.rfind('a')+ 1
print("Quantidade de vezes que 'a' letra a aparece:  {} vezes ".format(repeticao))
print("Posição em que aletra 'a' aparece pela primeira vez: {} posição".format(posicao1))
print("Posição em que aletra 'a' aparece pela última vez: {} posição".format(posicao_final))