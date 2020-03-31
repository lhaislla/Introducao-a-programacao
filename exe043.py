#Programa que lê o peso  e a altura de uma pessoa
#calcula o seu IMC e mostra seu status, de acordo com a tabela abaixo:
#- Abaixo de 18.5: Abaixo do peso
#- Entre 18.5 e 25: Peso ideal
#- 25 até 30: Sobrepeso
#- 30 até 40:Obesidadde
#- Acima de 40: Obesidaade móbida

peso = float(input('\033[3;36;mQual seu peso? '))
altura = float(input('\033[3;36;mQual sua altura? '))
imc = peso /(altura**2)
print('O IMC dessa pessoa é: {:.2f}'.format(imc))
if imc <= 18.5:
    print('\033[3;36;mAbaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('\033[3;36;mPeso ideal')
elif imc >= 25 and imc <= 30:
    print('\033[3;36;mSobrepeso')
elif imc >= 30 and imc <= 40:
    print('\033[3;36;mObesidade')
else:
    print('\033[3;36;mObesidade Morbida')
