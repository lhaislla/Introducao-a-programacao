#Programa que lê o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
#Caso esteja errado, peça a digitação novamente até ter um valor correto
r = 'F', 'M'
sexo = str(input('Informe seu sexo: [M/F]  ')).strip().upper()[0]
while sexo not in 'FMmf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: '))
print('Sexo registrado com sucesso!')
