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


#-----------------------------------------------------------------------------------------------------------------------
##Main##      

print("Como criar alunos?")

aluno1 = Aluno("Zé",19,12345,"TSI")    #esse é só um elemento do tipo aluno
aluno2 = Aluno("Maria",20,6789,"TSI") 


aluno1.imprimeTudoJunto()
print("\n===========================================================================")
aluno2.imprimeTudoJunto()



aluno1.MudaCurso("Medicina")

#Acrescente um metodo p/ mudar o nome do curso do aluno. Em seguida, testem sem mudar o metodo imprimeTudoJunto




