#Algoritmo que lê  o preço de um produto e mostra seu novo preço, com 5% de desconto

preco=float(input("preço do produto:R$  "))
desconto=preco- (preco*(5/100))
print('Novo preço: R${:.2f}'.format(desconto))