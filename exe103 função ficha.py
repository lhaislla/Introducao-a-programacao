# Programa mostra a ficha do jogador , meso que algum dado não tenha sido informado
def ficha(jogador = ' ',gols= 0):
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato')
n = str(input('Nome do jogador:'))
g=int(input('Numero de gols:'))
if g.isnumeric():
    g=int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n, g)


