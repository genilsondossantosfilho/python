# Metodo pra criar a classse dos elementos individualmente da fila 
class UnidadesFila:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

# Metodo pra criar a classe do conjunto fila
class Fila:
    def __init__(self):
        self.primeiro = None

    def ImprimeFila(self):
        print("\n") #espaçamento

        aux = self.primeiro

        if aux is not None: #Perguntar se a Fila n esta vazia
            while aux is not None:
                print(aux.valor)
                aux = aux.proximo
        else:
            print("--- Fila Vazia ---")

        print("\n") #espaçamento



    def Enfileirar(self,Qualquervalor):  #Adicionar no final
        aux = self.primeiro

        if aux is not None: #n ta vazia
            while aux.proximo is not None:
                aux = aux.proximo
            aux.proximo = UnidadesFila(Qualquervalor, None)

        else: #vazia
            self.primeiro = UnidadesFila(Qualquervalor, None)



    def RemoveUnidadesFila(self):
        aux = self.primeiro

        if aux is not None: #n ta vazia
            self.primeiro = aux.proximo
            # return aux     quando o metodo for chamado ele n retorna mais None, mas sim, aux
            del aux   #eu precisaria tirar se fosse pra chamar fora do metodo

        else: #a lista ta vazia
            print("A lista ja esta vazia, n ha o que apagar")



    def DesenfileirarUmPorUm(self):    #limpar a fila toda mas, um nó de cada vez
        aux = self.primeiro

        if aux is not None:  #cheia
            while aux is not None: 
                self.primeiro = aux.proximo
                del aux
                aux = self.primeiro




    def DesenfileirarTodosDeUmaVez(self):    #limpar a conexao do self ao 1 elemento, deixando o resto da lista solta na memoria. ai o garbage collector apaga os objetos automaticamente
        self.primeiro = None
            


# --- CRIANDO MANUALMENTE  ---


ListaFila = Fila()  #criei um objeto fila

#adcionar elementos nessa fila

# ListaFila.self.primeiro = uf1   O self só existe dentro dos métodos da classe. Fora da classe, nunca use self. 

# ListaFila.primeiro = uf1   precisa criar primeiro e depois apontar

# uf3 = UnidadesFila("maçã")
# uf2 = UnidadesFila("banana",uf3) 
# uf1 = UnidadesFila("abacaxi",uf2) 

# ListaFila.primeiro = uf1 


ListaFila.Enfileirar("maçã")
ListaFila.Enfileirar("banana")
ListaFila.Enfileirar("abacaxi")

# teste = ListaFila.RemoveUnidadesFila()  aux do metodo de remoçao
 
# ListaFila.RemoveUnidadesFila()
ListaFila.DesenfileirarTodosDeUmaVez()
ListaFila.ImprimeFila()

# print(teste.valor)   chamar o aux do metodo de remoçao 


   
   
