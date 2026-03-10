class Elemento:
    def __init__(self, valor, proximo):
        self.valor = valor
        self.proximo = proximo



from Elemento import Elemento

class Lista:
    def __init__(self):
        self.primeiro = None



## MAIN ##
# I passo - CRIE A LISTA
minhaLista = Lista()

# II passo - CRIE OS ELEMENTOS
elemento1 = Elemento(1, None)
elemento2 = Elemento(2, None)
elemento3 = Elemento(3, None)
elemento4 = Elemento(4, None)
elemento5 = Elemento(5, None)
elemento6 = Elemento(6, None)
elemento7 = Elemento(7, None)
elemento8 = Elemento(8, None)
elemento9 = Elemento(9, None)
elemento10 = Elemento(10, None)

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

# Percorrer e imprimir elementos da lista encadeada
# aux = minhaLista.primeiro
# while aux is not None:
#     print(aux.valor)
#     aux = aux.proximo
