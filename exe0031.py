#Programa que pergunta a distância da viagem em Km
#Calcula o preço da passagem
#cobrando R$ 0.50 por km para viagens de até 200 km
#e cobrando R$ 0.45 para viagens mais longas

distancia = float(input('\033[1;;41mQual a distância percorrida? '))
print('\033[1;;41m-*-' * 30)
if distancia <= 200:
    print('\033[1;;41mO valor da passagem para os {} km/h percorridos é de: R$ {}'.format(distancia,(distancia*0.50)))
else:
    print('\033[1;;41mO valor da passagem para os {} km/h percorridos é de: R$ {}'.format(distancia,(distancia*0.45)))
print('\033[1;;41m-*-' * 30)
#print('''Outra forma de fazer: If line ou if simplificado:
# preco = distancia* 0.50 if distancia <= 200 else distancia * 0.45''')


