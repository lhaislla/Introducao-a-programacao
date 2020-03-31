#Programa que lê a largura e altura de uma paredde em metros, calcula a sua área e a quantidade de tinta necessáia para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area= largura * altura
quantidade_de_tinta= area /2
print('A área da parede é {:.3f}m² e a quantidade de litros de tinta para pintar a parede é de {}litros '.format(area,quantidade_de_tinta))
