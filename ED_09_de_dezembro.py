import Elemento


class Lista:
    def __init__(self):
        self.primeiro = None

    def imprimeLista(self):
        aux = self.primeiro
        if aux is not None:
            while aux is not None:
                print(aux.valor)
                aux = aux.proximo
        else:
            print("--- Lista Vazia ---")

    # fábrica de criar elementos
    def criarNovoElemento(self, valorQualquer):
        return Elemento(valorQualquer, None)

    # adicionar no final
    def addElementoNoFinal(self, valorQualquer):
        if self.primeiro is None:
            self.primeiro = self.criarNovoElemento(valorQualquer)
            ultimo = self.criarNovoElemento(valorQualquer)
            self.ultimo = self.primeiro.proximo 
        else:
            aux = self.primeiro
            while aux.proximo is not None:
                aux = aux.proximo
            aux.proximo = self.criarNovoElemento(valorQualquer)
            aux.proximo.proximo = self.ultimo
            

    # adicionar no início
    def addElementoNoInicio(self, valorQualquer):
        novo = self.criarNovoElemento(valorQualquer)
        novo.proximo = self.primeiro
        self.primeiro = novo



   



    # -------------------------------
    # MÉTODOS DE REMOÇÃO
    # -------------------------------

    # 1) Remover o primeiro elemento
    def removeInicio(self):
        aux = self.primeiro
        
        if self.primeiro is None:
            print("Lista já está vazia")
            return
        
        self.primeiro = self.primeiro.proximo
        del(aux) #precisa deletar a variavel pois continua ocupando espaco se eu so apontar, ela fica perdida na memoria mas ainda esta la


    # 2) Remover o último elemento
    
    def removeFinal(self):
        if self.primeiro is None:
            print("Lista já está vazia")
            return

        # Se só tiver um elemento
        if self.primeiro.proximo is None:
            self.primeiro = None
            return

        # Se tiver mais de um
        aux = self.primeiro
        while aux.proximo.proximo is not None:
            aux = aux.proximo

        # aux está no penúltimo nó
        aux.proximo = None


    # 3) Remover elemento pelo valor
    def removeValor(self, valor):
        if self.primeiro is None:
            print("Lista vazia")
            return

        # Se for o primeiro
        if self.primeiro.valor == valor:
            self.primeiro = self.primeiro.proximo
            return

        # Procurar o elemento anterior ao que será removido
        aux = self.primeiro
        while aux.proximo is not None and aux.proximo.valor != valor:
            aux = aux.proximo

        # Não encontrou
        if aux.proximo is None:
            print("Valor não encontrado na lista")
            return
  # -------------------------------
    # MÉTODOS DE REMOÇÃO
    # -------------------------------

        # Remove pulando o nó
        aux.proximo = aux.proximo.proximo


## MAIN ##
# I passo - CRIE A LISTA
minhaLista = Lista()

# II passo - CRIE OS ELEMENTOS
elemento1 = Elemento.Elemento(1, None)
elemento2 = Elemento.Elemento(2, None)
elemento3 = Elemento.Elemento(3, None)
elemento4 = Elemento.Elemento(4, None)
elemento5 = Elemento.Elemento(5, None)
elemento6 = Elemento.Elemento(6, None)
elemento7 = Elemento.Elemento(7, None)
elemento8 = Elemento.Elemento(8, None)
elemento9 = Elemento.Elemento(9, None)
elemento10 = Elemento.Elemento(10, None)

# III passo - ENCADEIE OS ELEMENTOS
minhaLista.primeiro = elemento1
elemento1.proximo = elemento2
elemento2.proximo = elemento3
elemento3.proximo = elemento4
elemento4.proximo = elemento5
elemento5.proximo = elemento6
elemento6.proximo = elemento7
elemento7.proximo = elemento8
elemento8.proximo = elemento9
elemento9.proximo = elemento10




minhaLista.addElementoNoFinal(11)
minhaLista.imprimeLista()
