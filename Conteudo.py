print('''#Cadeias de caracteres
#strings
#Toda cadeias de texto está entre "" ou ''

#frase = 'curso em video python' \
#indice é um número sequencial de zero até a quantidade que precisa pra escrever
#print(frase[11],frase[1],frase[9],frase[10],frase[11],frase[13])

#Fatiamento
#frase[valor_da_posição]: pega o que estiver escrito na posição especificada
#frase[posição_inicial:posição_final]:pega o que está escrito de um valor até o valor anterior ao fim expecificado
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


#TRansformação de strings(imutavel, que só muda por meio de métodos)

#frase.replace( 'Python', 'Android'), replace significa reposicionar essa função troca uma palavra por outra
#frase.upper()= Fica em maiusculas as letra(o que já é maiusculo é mantido, o que era minusculo vira mausculo
#frase.lower()= fica minuscula, o que já era minuscula fica minuscula e o que era maiuscula fica minuscula
#frase.captalize() = Joga todos os caracteres para minusculo e só o primeiro caractere fica em maiusculo
#frase.title()=Analisa quantas palavras tem essa string, por meio das posições do espaço e faz captalize palavra por plavra
#frase.strip()= remove todos os espaços inuteis do inicio e do fim da string
#frase.rstrip() = remove os espaços vazios da direita (r de right, direita)
#frase.lstrip() = remove os espaços vazios da esquerda(l de left, esquerda)

#Divisão de string
#frase.split()= divisão dentro da string considerando os espaços,gera uma lista com todas as palavras com uma cadeia d caracteres
#'-'.join(frase)= juntar todos os elementos de frase usando o separador -

#print para escrever em outra linha: print(""" hajhhshjashjh""")''')
print('''
Estruturas Condicionais
    -Estrutura sequênciaç: feito em um uma sequência;
    -Algoritmo: COnjunto de passos;
    -Identação;
if:(se) 
else:(se não)
elif:
   Exemplo:
   if carro.esquerda():
        bloco True
    else:
         Bloco False 

while:
for:


''')
print('''#Exemplo1 (Condições simples, condições compostas e condições simplificadas)
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('carro novo')
else:
    print('Carro velho')
print('--Fim---')


#Exemplo2
nome = str(input('Qual seu nome? ')).title()
if nome == 'Lhaislla':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão estranho')
print('Bom dia, {}! '.format(nome))

n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
media = (n1+n2) /2
print('A sua média foi {:.1f}'.format(media))
if n1 >= 10.0 and n2>= 10.0 :
    print('Notas invalidas! ')

else:
    if media >= 6.0:
        print('Sua média foi boa, parabéns!')
    else:
        print('Sua média foi ruim, estude mais!')
#Obs:print('parabéns' inf media>=6.0 else 'Estude mais!')''')





l





