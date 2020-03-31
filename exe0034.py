# Programa que pergunta o alário do funcionário
#Calcula o valor do aumento
#Para salários superiores a R$ 1.250.00 calcula um aumento de 10¢
#Para salários inferiores a R$ 1.250.00 calcula um aumento de 15¢
salario = float(input('Digite seu salário: '))
print('-*-' * 20)

if salario <= 1250:
    novo =  salario + (salario*15/100)
    print('O seu aumento é de 15% e seu salário passa a ser: R$ {:.2f} '.format(novo))
else:
    novo = salario + (salario * 10 / 100)
    print('O seu aumento é de 10% e seu salário passa a ser: RS {:.2f} '.format(novo))
print('-*-' * 20)