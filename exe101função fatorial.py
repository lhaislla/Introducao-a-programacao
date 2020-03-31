def fat(n=0):
    f=1
    for i in range(n,1,-1):
        f *= i
    return(f)
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a  {fat(n)}')
