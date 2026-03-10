# Metodo pra criar a classse dos elementos individualmente da pilha 
class UnidadesPilha:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

# Metodo pra criar a classe do conjunto pilha
class Pilha:
    def __init__(self):
        self.primeiro = None

    def ImprimePilha(self):   #imprime ao contrario, do ultimo ate o primeiro 4, 3, 2, 1
        print("\n") #espaçamento

        aux = self.primeiro

        if aux is not None: #Perguntar se a Pilha n esta vazia
            while aux is not None:
                print(aux.valor)
                aux = aux.proximo
        else:
            print("--- Pilha Vazia ---")

        print("\n") #espaçamento



    def Empilhar(self,Qualquervalor):  #Adicionar no final (inicio)

        if self.primeiro is not None: #n ta vazia
            new = UnidadesPilha(Qualquervalor, None)
            new.proximo = self.primeiro
            self.primeiro = new
            

        else: #vazia
            self.primeiro = UnidadesPilha(Qualquervalor, None)



    def Desempilhar(self):  #Remove do final (inicio)
        print("\n") #espaçamento

        aux = self.primeiro

        if aux is not None: #n ta vazia
            self.primeiro = aux.proximo
            # return aux     quando o metodo for chamado ele n retorna mais None, mas sim, aux
            return aux   #eu precisaria tirar se fosse pra chamar fora do metodo

        else: #a lista ta vazia
            print("A Pilha ja esta vazia, n ha o que apagar")

        print("\n") #espaçamento


    def DesemPilharUmPorUm(self):    #limpar a pilha toda mas, um nó de cada vez
        print("\n") #espaçamento

        aux = self.primeiro

        if aux is not None:  #cheia
            while aux is not None: 
                self.primeiro = aux.proximo
                del aux
                aux = self.primeiro

        else: #a pilha ta vazia
            print("A Pilha ja esta vazia, n ha o que apagar")

        print("\n") #espaçamento


    def DesemPilharTodosDeUmaVez(self):    #limpar a conexao do self ao 1 elemento, deixando o resto da lista solta na memoria. ai o garbage collector apaga os objetos automaticamente
        self.primeiro = None
            

    def BuscarNaPilha(self, QualquerValor, aux=None):  #minha funçao começa podendo receber ate 3 parametros. o aux e uma variavael que eu posso usasr e pra cria-la preciso definir um apontamento default pra ela(None)
        print("\n") #espaçamento

        if self.primeiro != None:   #pilha cheia
            aux = self.primeiro

            if aux.valor == QualquerValor:
                return print("Achado o valor:", aux.valor)

            else:
                return self.BuscarNaPilha(QualquerValor, aux.proximo)

        else:             #pilha vazia
            return print("N encontrei o que pediu pq a pilha esta vazia")

        print("\n") #espaçamento





# --- CRIANDO MANUALMENTE  ---


Pilha = Pilha()



Pilha3 = UnidadesPilha("c")
Pilha2 = UnidadesPilha("b",Pilha3)
Pilha1 = UnidadesPilha("a",Pilha2)

Pilha.primeiro = Pilha1

Pilha.Empilhar("2")

# Pilha.Desempilhar()
# Pilha.DesemPilharTodosDeUmaVez()


# Pilha.ImprimePilha()
   
Pilha.BuscarNaPilha(2)
#por um metodo de busca aqui usando recursividade
   
