#Estruturas Compostas
#Tuplas
print('''variavel simples:
       lance = comida
Variavel composta:
    strings
    tuplas(usar fatiamento para e expecificar a informação) ()
    listas []
    dicionario {}
Tuplas : é uma variavel que guarda mais de um valor 
    Os elementos são indentificados por números
    Tuplas são IMUÁVEIS
''')
#Manipulação de tuplas
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata-Frita'
print('\033[;32;m{}'.format(lanche))
#maneira sem precisar da posição:
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi ra caramba!')

#outra maneira (mostra a posição)
for cont in range(0, len(lanche)):
    print(lanche[cont])

#outra maneira com enumerate que dá tanto o dado quanto a posição
#Além do dado dá a posição
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata-Frita'
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida } na posição {pos}')
#função sorted() coloca as coisas da tuplas em ordem alfabetica 
print(sorted(lanche))

#variavel.count(o que deseja saber)
#.index() indica a posição
a = 2, 5, 4
b = 5, 8, 1, 2
c = b+a
print(c.count(5))
print(sorted(c))
print(c.index(5,1))


#Apagando uma tupla(apagar a tupla inteira)
pessoa = 'gustavo', 39, 'M', '99.88'
del(pessoa)
print(pessoa)






