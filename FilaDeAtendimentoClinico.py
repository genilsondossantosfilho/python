     
from Paciente import Paciente


class FilaDeAtendimentoClinico:
    def __init__(self):
        self.first = None
        self.last = None

    def Entrar(self,a1):  #adcionar mais um paciente na fila (no final)
        new = Paciente(a1,None)

        if self.first == None:  #fila vazia

            self.first = new
            self.last = new
            new.next = None

        else: #fila ja tem gente esperando
            self.last.next = new
            self.last = new
            new.next = None


    def Atender(self):

        if self.first == None:  #fila vazia
            print("Não tem ninguem pra ser atendido.\n")
       
        else: #fila ja tem gente esperando
            saindo = self.first
            self.first = self.first.next
            print(f"{saindo.nome} acabou de ir embora da fila. \n")
           


    def Mostrar(self):

        if self.first == None:
            print("A fila esta vazia...\n")

        else:
            aux = self.first  

            while aux != None:
                print(aux.nome)
                aux = aux.next
