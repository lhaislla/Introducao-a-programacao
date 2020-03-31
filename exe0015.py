#Aluguel de carro(Quantidade de quilometros percorridos por um crro alugado, quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado)

km=float(input("Qual a quantidade de Km percorridos? "))
dias=int(input('Qual a quantidade de dias que o carro foi alugado?'))
preco_a_pagar= (60*dias)+(0.15*km)
print("O preço a pagar: R$ {:.2f}".format(preco_a_pagar))