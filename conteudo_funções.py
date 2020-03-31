"""
Funções:

    -Rotina(coisa que se faz constantemente)
    - O programa só executa suas funções quando são chamadas
    - Cria comando personalizados
    - sum soma todos os elementos de uma lista


"""
#Precisa declarar uma variavel como paramêtro e chamar na função
#
#Exemplo:

'''def mostralinha():
    return (print('\033[1;33;m-'*40))

def mensagem(msg):
    mostralinha()
    print(msg)
    mostralinha()
mensagem('SISTEMA DE ALUNOS   ')
def titulo(txt):
    print('\033[1;32;m-'*40)
    print(txt)
    print('-' * 40)
titulo('CURSO EM VIDEO')
titulo('PYTHON É MUITO BOM')
def soma(a,b):
    s= a+b
    return(s)

soma(2,1)
'''

'''
    -   Empacotar parametros
    -   Cria um contador 
'''
#Tipo um ponteiro
'''def contador(*num):
    for valor in num:
        print(valor)
    tam = len(num)
    print(num)
    print(f'Tamanho de num: {tam}')
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
#funções com listas

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos += 1
    print(lst)
valores=[7,2,5,0,4]
dobra(valores)'''

#A passagem de parametros em python é por referencia

def soma(*valores):
    s=0
    for n in valores:
        s+= n
    print(f'Somando os {valores}  temos {s}')
soma(7,3)
print(input,__doc__)

'''
    - Interactive Help
        help()
            entrar na  ajuda interativa 
        quit()
            sair da ajuda interativa
        help(função)
    print(input__doc__)
            
    - Docstrigs
        Uma string de documentação
        essas aspas que estou usando, servem para fazer um manual completo da função
         só colocar  as aspas na primeira linha da função e dar enter
    - Argumentos/parametros opcionais
        colocar no parametro um igual a vazio no parametro que não será usado 
        
    - Escopo de variáveis 
        Local onde  a variavel vai existir 
        ou local onde a variavel não vai existir
        Escopo local: A variavel só irá existem naquela função
        Escopo global: a variavel existe em toda parte do programa 
        ex:
    def teste(b):
        b+= 4
        c= 2
        print(f'A dentro vale{a}')
        print(f'B dentro vale {b}')
        print(f'C dentro vale {c}')
    a=5
    teste(a)
    print(f'A fora vale {a})
        quando expecificaca uma váriavel global dentro da função 
        ( esta dizendo para que use a variavel global, mesmo que exista uma variavel local de mesmo nome)
        Só usa  variaveis globais dentro d afunção se expeficar que a variavel é uma global 
        
    - Retorno de resultados
        As funções  em python podem não retonar(imprimir dentro delas) ou retornar um valor 
        return
        ex:
            def soma(a=0,b=0,c=0):
            s = a+b+c
            return(s)
    Guarda os valores(são uteis quando quer ter personalização dos resultados)
    O return não é apenas para números
    
'''

'''Parametros != Argumentos:
    - parametros são declarados na função
    - argumentos são atribuições de valores as funções
    - Parametros default: Parametros que são definidos dentro da função
    
 
 '''
'''
def login(usuario = 'root',senha='123'):
    print(f'Usuario:{usuario}')
    print(f'Senha: {senha}')

login('lhaislla','77')

def func():
    return 1,2
a,b = func()
print(a)
print(b)'''
#Retorno de multiplos valores:
'''def potencia(a):
    potq= a** 2
    potc= a** 3
    return potq,potc

q,c = potencia(10)
print(q)
print(c)'''

'''#Funções variádica:Funções que recebem uma quantidade variavel de parametros:
    - Parametros precedidos por * é capaz d ereber uma lista de parametros 
    posicionais .
    - Todos os  parametros precedidos por ** poderá receber um conjunto 
    deprametros nomeados (QUando associa o nome do argumento com o valor ).
    -
    
    '''
#quando não souer a quantidade de valores que será associado a uma funçõa
#Funções capazes de receber uma quantidade arbitraria de valores
def lista_de_argumentos(*posicionais):
    print(posicionais)
#lista_de_argumentos(1,2,3,4,5,6)
def contador(*num):
    print(num)

#contador(1,2,3,4,5,6)
#lista_de_argumentos("um",'dois','três')

#Passagem de agumentos associativos
def lista_de_argumentos_associativos(**associados):
    print(associados)

#lista_de_argumentos_associativos(a=1,b=2,c=3,d=4)

def argumentos(*posicionais,**associados):
    print(posicionais,associados)
argumentos(1, 2, 3, 4, um=1, dois=2, tres=3, quatro=4)
