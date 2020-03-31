#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$ 7.00 por cada km camia do limite

velocidade = float(input('\033[1;;41mQual a velocidade do carro? '))
print('\033[1;;41m-*-' * 20)
if velocidade >= 80:
    print('\033[1;;41mVocê foi multado, pois estava á {} km/h onde o límite de velocidade é de 80km/h'.format(velocidade))
    print('\033[1;;41mO valor da multa é de R${:.2f}'.format((velocidade-80)*7))
else:
    print('\033[1;;41mTenha um bom dia! Dirija com segurança!')

print('\033[1;;41m-*-' * 20)