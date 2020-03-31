#Programa que checa se os há paresde parenteses corretos na expresão
pilha = []
exp=(str(input('Digite uma expressão: ')))
for simb in exp:
    if simb in exp:
        if simb == '(':
            pilha.append('(')
        elif simb == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')
                break

if len(pilha)== 0:
    print('Sua expressão  está válida!')
else:
    print('Sua expressão está errada! ')
