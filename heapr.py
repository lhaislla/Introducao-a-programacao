def heapify (a,tam):
    p= (tam //2)-1
    while p>0:
        menortam(a,p,tam)
        p-= 1

def siftdow (a, i,
             tam):
    l = (2 * i)+1
    r = (2 * i)
    + 2
    largura = i
    if l <= tam -1 and a[l] > a[i]:
        largura = l
    if r <= tam-1 and a[r] > a[largura]:
        largura = r
    if largura != i:
        swap (a,i,largura)
        siftdown (a,largura,tam)
