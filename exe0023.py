#Fatiamento
#fraae[valor_da_posição]: pega o que estiver escrito na posição especificada
#frase[posição_inicial:posição_final]:pega o que está escrito de um valor até o valor anterial ao fim expecificado
#frase[posição_de_começo: posição_de_parada: intervalo_que_quer_pegar_as_letras]
#frase[:5] = antes dos : é onde ele vai começar,sendo o valor expecificado seu fim
#frase[15:]= indica do incio sem saber o final(fatia a frase inteira
#frase[9::3]= começa no nove e vai até o final, pulando de 3 em 3.

#Análise de string
#len[frase]= comprimento da frase
#frase.count('o')= conta quantas vezes aparece uma letra
#frase.count('o',0,13) = contagem com fatiamento
#frase.find('deo')= quantas vezes ele encontro deo na frase (find é encontrar),econtra deo começando de uma posição
#caso o find esteja um valor que não existe ele retorna -1
#in= 'curso' in frase : se axiste a palavra curso na frase; retorna True ou False

#Programa que lê um número qualquer na tela e mostra na tela cada um dos digitos separados

valor=int(input('\033[1;;46mDigite um valor: '))
n= str(valor)
#tamanho = varlor.strip()
unidade = valor//1 % 10
dezena = valor//10 % 10
centena = valor//100 % 10
milhar = valor//1000 % 10
print('\033[1;;44munidade:',unidade)
print('\033[1;;47mdezena:',dezena)
print('\033[1;;46mcentena:',centena)
print('\033[1;;44mmilhar:',milhar )

