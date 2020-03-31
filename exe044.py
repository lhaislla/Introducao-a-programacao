#Programa que calcula o valor a ser pago por um produto
#Considerrando o seu preço normal
#Condições de pagamento:
#- Á vista dinheiro / cheque: 10% de desconto
#- Á vista no cartão: 5% de desconto
#- Em até 2X no cartão: Preço normal
#- 3X ou mais no cartão: 20% de juros.

preco_produto = float(input("\033[;37;mPreço do produto: "))
print('''\033[;34;m
Opções de pagamento:

    1- Á vista em dinheiro ou em cheque: 10% de desconto
    2- Á vista no cartão: 5% de desconto 
    3- Em até 2x no cartão: Preço normal 
    4- 3x ou mais no cartão: 20% de juros.

''')
opcao = int(input('\033[;34;mSelecione sua opção de pagamento: '))
if opcao == 1:
    valor = preco_produto - 10 /100 * preco_produto
    print('\033[;35;mValor de a vista em dinheiro ou cheque: R${:.2f}'.format(valor))
elif opcao == 2:
    valor = preco_produto - ( 5 /100 * preco_produto)
    print('\033[;35;mÁ vista no cartão: R${:.2f}'.format(valor))
elif opcao == 3:
    quantidade_parcelas = int(input('Quantidade de parcelas: '))
    if opcao == 3 and quantidade_parcelas  <=2:
        valor = (preco_produto / quantidade_parcelas)
        print('\033[;35;m{}x no cartão com parcela(s) de: R${:.2f} '.format(quantidade_parcelas,valor))
    else:
        print('\033[;31;mQuantidade de vezes no cartão é maior que 2x')
elif opcao == 4:
    quantidade_parcelas = int(input('Quantidade de parcelas: '))
    if quantidade_parcelas  > 2:
        valor = (preco_produto + (20 /100)* preco_produto)/quantidade_parcelas
        print('\033[;35;m{}x no cartão: R${:.2f}'.format(quantidade_parcelas,valor))
    else:
        print('\033[;31;mOpção de pagamento errada ')
else:
    print('\033[;31;mOpção de escolha invalida ')
