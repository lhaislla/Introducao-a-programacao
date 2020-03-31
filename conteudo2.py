
print(''' 
#Estrutura de controle
    Laços,Repetições ou Iterações.
Exemplo do personagem andando
for(para)
fazer um contador
laco c no intervalo(1,10)
    passo
pega.
for c in range(1,10:

laco c intervalo(0,3)
    passo 
    pula
passo 
pega
laco c no intervalo(0,3)
    se moeda:
        pega
    passo
    pula
passo
pula
pega


Obs:range(Valor_inicial,Valor_final)
percorre lendo todos os valores

         ''')
for c no in range(1,10):
    passo
pega.
for c in range(0,3):
    passo
    pula
passo
pega

for c in range(1,3):
    passo
    pula
    passo
pega

#Na contagem em python ele ignora o último número
#range(Valor_inicial,Valor_final)
#Para que a contagem seja nos entido inverso(contar pra trás:range(Valor_final,Valor_inicial,-Quantidade_que_deseja_voltar)
i = int(input('Início: '))
f =int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')
#Contador
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi: {} '.format(s))