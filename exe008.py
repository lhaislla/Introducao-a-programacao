#Programa que converte para metros
menu= 'Menu'
op1= '\033[;;4m1° Digite 1 se quiser transformar de milímetros para metros'
op2= '\033[;;40m2° Digite 2 se quiser transformar de centímetros para metros'
op3= '\033[;;40m3° Digite 3 se quiser transformar de decímetros para metros'
op4= '\033[;;40m4° Digite 4 se quiser transformar decâmetro de  para metros'
op5= '\033[;;40m5° Digite 5 se quiser transformar hectómetro de  para metros'
op6= '\033[;;40m6° Digite 6 se quiser transformar quilómetro de  para metros'

print('Menu:')
print('\033[;;40m{}'.format(op1))
print('\033[;;401m{}'.format(op2))
print('\033[;;40m{}'.format(op3))
print('\033[;;40m{}'.format(op4))
print('\033[;;40m{}'.format(op5))
print('\033[;;40m{}'.format(op6))

opcao= int(input('\033[;;46mopção de conversão: ' ))

if opcao == 1:
    n=float(input("\033[;;47mDigite o valor que deseja transformar: "))
    result = n/(1000)
    print('\033[;;40mO valor de Milímetros para metros é: {}'.format(result))
elif opcao == 2:
    n = float(input("Digite o valor que deseja transformar: "))
    resul = n / (100)
    print('\033[;;41mO valor de centímetrospara metros é: {}'.format(resul))
elif opcao ==3:
    n = float(input("Digite o valor que deseja transformar: "))
    resu = n / (10)
    print('\033[;;41mO valor de decímetros para metros é: {}'.format(resu))
elif opcao ==4:
    n = float(input("\033[;;41mDigite o valor que deseja transformar: "))
    res = n * (10)
    print('\033[;;41mO valor de decâmetro para metros é: {}'.format(res))
elif opcao ==5:
    n = float(input("\033[;;41mDigite o valor que deseja transformar: "))
    re = n * (100)
    print('\033[4;33;41mO valor de hectómetro para metros é: {}'.format(re))
else:
    n = float(input("\033[;;41mDigite o valor que deseja transformar: "))
    r = n * (1000)
    print('\033[6;32;41mO valor de quilómetro para metros é: {}'.format(r))


#medida - float(input('uma distância em metros: ")
#cm = medida * 100
#mm= medida * 1000
#print("medida de {}m correspondente a {}cm e {}mm".format(medida,cm,mm))
