#Programa pra aprovar um emprestimo bancario da compra de uma casa
#Perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal,
#sabendo que a prestção não pode exceder 30% do salário ou então o empréstimo será negado
#Se pode ou não comprar a casa

valor_da_casa = float(input('\033[1;31;mQual o valor da casa: '))
salario = float(input('\033[1;31;mSalário do comprador: '))
quantos_anos = int(input('\033[1;31;mEm quantos anos o comprador vai pagar a casa: '))
prestacao_anual = valor_da_casa / quantos_anos
prestacao_mensal = valor_da_casa / (quantos_anos*12)
limite =  30 / 100 * salario
if   prestacao_mensal <=limite:
    print('\033Parabéns! A compra do imovel foi aprovada!')
    print('\033[1;36;mParecelas anuais de: R${:.2f} e parecelas Mensais de: R${:.2f}'.format(prestacao_anual,prestacao_mensal))
else:
    print('\033[1;36;mInfelizmente você não pode financear essa casa! ')





