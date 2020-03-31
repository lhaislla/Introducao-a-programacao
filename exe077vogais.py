#Programa que retira as vogais
palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar')
for p in palavras:
    print(f'\nNa palavra {p.upper} temos')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')

