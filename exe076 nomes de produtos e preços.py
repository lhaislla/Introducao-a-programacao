# Programa que cria uma tupla com nome e preço dos produtos.
# No final mostra uma listagem de preços .
# organizando os dados em forma tabular.
lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Estojo', 15.90,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas',  22.30,
         'Livro', 34.90)
print('-' *40)
print(f'{"LISTAGEM PREÇOS":^40}')
print('-' *40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end ='')

    else:
        print(f'{lista[pos]:>7.2f}',)
print('-' *40)
