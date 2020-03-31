# Programa que coloca vário números em uma lista
# Mostra quantos núemros foram digitados
# Ordena os valores de forma decrescente
# Checa se o valor 5 foi digitado e está ou não na lista

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).upper()
    if r in 'N':
        break
lista.sort(reverse=True)
print(f'Quantidade de valores na lista:{len(lista)}')
if 5 in lista:
    print('O número 5 está na lista ')
else:
    print('Não achei o número 5')
print(f'Os valores em ordem decrescente são: {lista}')
