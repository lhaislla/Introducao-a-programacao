# Programa cadastro de valores em uma lista
# Pela posição de inserção
lista = []
for cont in range(0,5):
    valor=(int(input('Digite um valor:  ')))
    if cont == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {lista}')
