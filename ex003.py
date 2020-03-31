# Tipos primitivos:
#string: str=letras,palavras
#inteiros: int= números negativos,positivos ou nulos
#float: foat= números reais, ponto futuante,(com virgulas e pontos, monetarios)
#bool: bool=(True ou False)

#print('A soma vale{}'.format{variavel que_tem_a_informação})= substituida por um metodo da própria string
#Para saber qual o tipo primitivo de uma variavel: type(variavel_a_ser_analisada)
#.isnumeric() pra perguntar se é um número
#.isalpha() pra perguntar se é uma letra
#.isupper pra perguntar se tem uma pavra na frase

n1 = int(input("Digite o primeiro valor:  "))
n2 = int(input("Digite o segundo valor:  "))
result = n1 + n2
#print("O resultado da soma de dois números: ",resultado )
print('\033[5;36;41mA soma entre {} e {} vale {}'.format(n1 , n2, result))
