def complementar(L,U):
  complementar=[]
  for x in range(1,int(U)+1):
    if str(x) not in L:
      complementar.append(x)
  return complementar
def unicao(A,B):
  unição = []
  for x in B:
    unição.append(x)
  for x in A:
    if x not in unição:
      unição.append(x)
  return unição
def intersecao(A,B):
  Intersecao =[]
  for y in B:
    for x in A:
      if x == y:
        Intersecao.append(y)
  return Intersecao

def tirar(origem,parte):
  saida=[]
  for x in origem:
    if x not in parte:
      saida.append(x)
  return saida
U=int(input("Qual tamanho do universo!"))
entradaA =input("Conjunto A: ").split()
entradaB=input("Conjunto B: ").split()
print("A = ",entradaA)
print("B = ",entradaB)
print("O complementar de A : ",complementar(entradaA,U))
print("O complementar de B : ",complementar(entradaB,U))
print("A Unição B = :",unicao(entradaA,entradaB))
print("A interseção B = :",intersecao(entradaA,entradaB))
print("A - B = ",tirar(entradaA,entradaB))
print("B - A = ",tirar(entradaB,entradaA))

