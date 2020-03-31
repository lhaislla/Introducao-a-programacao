#Algoritmo que lê o salário de um funcionário e mstra seu novo salário, com 15% de aumento.
salario=float(input('Digite o salário:R$ '))
aumento= salario*(15/100)
novo_salario= salario+aumento
print('Novo salário: R${:.2f}'.format(novo_salario))
print(aumento)