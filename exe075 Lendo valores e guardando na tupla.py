#Programa que lê 4 valores e guarda na tupla
# Mostra quantas vezes apareceu o valor 9
# Em que posição foi digitado o primeiro valor 3
# Quais foram os números pares

n = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
quant9= n.count(9)

print(f'Você digitou os valore: {n}')
print(f'O número 9 apareceu {quant9} vezes')
if 3 in n:
    posi3 = n.index(3) + 1
    print(f'O valor 3 foi digitado na posição: {posi3}')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
print('Os valores pares foram: ',end='')
for i in n:
    if i % 2 == 0:
        print(i,end=' ')
