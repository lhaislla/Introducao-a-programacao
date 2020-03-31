# Progrma que lê 5 valores e guarda-os em uma lista
# Mostra qual foi o maior e o menor valor digitado
# E mostra as posições na lista as suas respectivas
valores = list()
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a Posição {cont}:  ')))
print(f'Você digitou os valores: {valores}')
print(f'Maior valor: {max(valores)}')
print(f'Menor valor: {min(valores)}')

