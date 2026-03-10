'''matrizes em python


valeria e nadja estutura de base de dados cavalcante e rodriguez
tanebau algoritimos e estruturas de dados
wikipedia
'''

class Aluno:
    def __init__(self,p1,p2,p3,p4):
        self.nome = p1
        self.idade = p2
        self.matricula = p3
        self.curso = p4 

    def imprimeTudoJunto(self):
        print("\n Nome do aluno:",self.nome)
        print("\n Data de nascimento do aluno:",self.idade)
        print("\n Idade do aluno:",self.matricula)
        print("\n Curso do aluno:",self.curso)

    def MudaCurso(self, novoCurso):
        self.curso = novoCurso


# #----------------------------------------------------------------------------------------------------------------------
# ##Main##      

# print("Como criar alunos?")

# aluno1 = Aluno("Zé",19,12345,"TSI")    #esse é só um elemento do tipo aluno
# aluno2 = Aluno("Maria",20,6789,"TSI") 


# aluno1.imprimeTudoJunto()
# print("\n===========================================================================")
# aluno2.imprimeTudoJunto()



# aluno1.MudaCurso("Medicina")

#Acrescente um metodo p/ mudar o nome do curso do aluno. Em seguida, testem sem mudar o metodo imprimeTudoJunto
class Elemento:
    def __init__(self,valor,proximo):
        self.valor = valor 
        self.proximo = proximo 






class Lista:
     def __init__(self):
        self.primeiro = None


# UmElementoQualquer = Elemento(1,None)
# UmElementoQualquer = Elemento(2,None)

# UmElementoQualquer1.proximo = UmElementoQualquer2






#crie a list 

minhaLista = Lista()



#crie os elementos 

elemento1 = Elemento(1,None)
elemento2 = Elemento(2,None)
elemento3 = Elemento(3,None)
elemento4 = Elemento(4,None)
elemento5 = Elemento(5,None)
elemento6 = Elemento(6,None)
elemento7 = Elemento(7,None)
elemento8 = Elemento(8,None)
elemento9 = Elemento(9,None)
elemento10 = Elemento(10,None)





#aponte esses elementos uns pros outros exceto o ultimo

minhaLista.primeiro = elemento1
elemento1.proximo = elemento2
elemento2.proximo = elemento3
elemento3.proximo = elemento4   #criar metodo pra criar esses vinculos
elemento4.proximo = elemento5 
elemento5.proximo = elemento6
elemento6.proximo = elemento7 
elemento7.proximo = elemento8
elemento8.proximo = elemento9
elemento9.proximo = elemento10


'''print(minhaLista)  #objeto em  enedereço de memoria 
print(minhaLista.primeiro)   #objeto atributo q aponta a outro objeto em
print(minhaLista.primeiro.valor)  #obj aponta a outro obj q aponta pra o atributo sai 1
print(minhaLista.primeiro.proximo.valor) # 2
'''
    



aux = minhaLista.primeiro

def imprimeLista(self):

    if aux != None:
        while (aux != None):
            print(aux.valor) 
            aux = aux.proximo

    else:
        print("Lista esta vazia")
   




def crieNovoElementoNoInicio(self,valorQualquer):
    aux = self.primeiro 

    if aux != None:
        novo = self.criarNovoElemento(valorQualquer)
        novo.proximo = self.primeiro

    else:
      





def crieNovoElementoNoFinal(self,valorQualquer):
    aux = self.primeiro

    if aux != None:
        while (aux.proximo != None):
            aux = aux.proximo

        aux.proximo = self.criarNovoElemento(valorQualquer)

    else:
        self.primeiro = self.criarNovoElemento(valorQualquer)
