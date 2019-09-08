resp = 'S'
n = quant = soma = maior = menor =0
while resp in 'S':
    n = int(input('\033[;32;mDigite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input(input('Quer continuar? [S/N] '))).upper().strip()[0]
media = soma / quant
print('\033[;36;mVocê digitou :{} e a média é :{}'.format(quant,média))
print('\033[;36;mO maior valor é: {} e o menor valor é: {}'.format(maior,menor ), end=' ')
