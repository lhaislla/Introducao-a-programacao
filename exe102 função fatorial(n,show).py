# função fatorial que recebe dois parametros número e show
#  Show será um valor lógico (opcional)
#  indicando se será mostrado ou não na tela o processo de cálculo do fatorial
def fatorial(n, show = False):
    f = 1
    for c in range(n, 0, -1):
        if  show:
            print(c, end='')
            if c > 1:
                print(f"{c} x ", end='')
            else:
                print('=', end='')
        f *= c
    return f
print(fatorial(5,show = True))