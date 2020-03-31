class no():
    def __init__(self, dado):
        self.dado = dado
        self.prox = None
        self.ant = None
    def pegaprox(self):
        return self.prox
    def pegaant(self):
        return self.ant
    def pegadado(self):
        return self.dado
    def trocaprox(self,novo):
        self.prox = novo
    def trocaant(self,novo):
        self.ant = novo

class lista():
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir(self,dado):
        novono =no(dado)
        if self.inicio == None:
            self.inicio = novono
            self.fim=novono
        else:
            self.fim.trocaprox(novono)
            novono.trocaant(novono)
            self.fim = novono

    def busca(self,dado):
        aux = self.inicio
        while aux != None:
            if aux.pegadado() == dado:
                return aux
            else :
                aux = aux.pegaprox()

        return False 
    def excluir(self, dado):
        aux = self.busca(dado)
        if aux == False:
            return "Valor não encontrado"
        elif aux == self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        elif aux == self.inicio:
            self.inicio = aux.pegaprox()
            self.inicio.trocaant(None)
        elif aux == self.fim:
            self.fim == aux.pegaant()
            self.fim.trocaprox(None)
        else:
            aux.pegaant().trocaprox(aux.pegaprox())
            aux.pegaprox().trocaant(aux.pegaant())

    def imprimir(self):
        if self.inicio == None:
            return "Lista vazia"
        aux = self.inicio
        impressao= str(aux.pegadado())
        
        while aux != None:
            impressao += " " +str( aux.pegadado())
            aux = aux.pegaprox()
        return impressao
        
        
