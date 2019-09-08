#Crie um programa que crie uma frase qualquer e diga se é um palindromo
#.join() desconsidera os espaços
frase =str(input('Digite uma frase: '))
palavra = frase.split()
junto = ''.join(palavra)
inverso= ''
print('o inverso de {} é {}'.format(junto,inverso))
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print(inverso)
if inverso == junto:
    print('A frase é um palindromo ')
else:
    print('A frase  não é um palindromo ')


