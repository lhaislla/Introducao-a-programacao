#Programa quelê quanto dinheiro uma pessoa tem na carteira e mostra quantos dólares ela pode comprar, considerando USS1,00=R$3,27
r=float(input('\033[1;;41mQuantos reais você tem na carteira? '))
d= 3.27
valor_de_real_para_dolar= r/d
print('\033[1;;41mO valor em dolar na sua carteira é de U${:.2f}'.format(valor_de_real_para_dolar))