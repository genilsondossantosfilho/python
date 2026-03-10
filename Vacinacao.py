
# ========================
# FUNÇOES DA FILA
# ==========================

class Elemento:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class FilaDeAtendimento:
    def __init__(self):
        self.primeiro = None
        self.contagem = 0
        self.ultimo = None


    def Enfileirar(self, qualquervalor):
        novo = Elemento(qualquervalor)

        if self.primeiro is None:
            self.primeiro = novo
            self.ultimo = novo
        else:
            self.ultimo.proximo = novo
            self.ultimo = novo

        self.contagem = self.contagem + 1 #pessoa


    def Desenfileirar(self):
        if self.primeiro is None:   #fila vazia, so tem o self primeiro
            return None


        saiu = self.primeiro   #apontamento pro primeiro elemento da fila q vai sair
        self.primeiro = self.primeiro.proximo # aponta pra um elemento a frente do primeiro, deixando o sem apontamentos, largado 

        if self.primeiro is None:   #fila vazia, so tem o self primeiro
            self.ultimo = None

        self.contagem = self.contagem - 1
        return saiu.valor


    def Imprimir(self):
        aux = self.primeiro

        while aux is not None:
            print(f"Nome: {aux.valor[0]} | CPF: {aux.valor[1]}")
            aux = aux.proximo




# ======================
# FUNÇOES DA PILHA
# ======================

class Doses:     #N ponha mais de uma classe em um mesmo arquivo, anotado
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo
        
        
class PilhaDeFrascos:
    def __init__(self):
        self.primeiro = None
        self.contagem = 0


    def Empilhar(self, valor):
        novo = Doses(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo
        self.contagem = self.contagem + 1

    def Desempilhar(self):
        if self.primeiro is None:
            return None

        saiu = self.primeiro
        self.primeiro = self.primeiro.proximo
        self.contagem = self.contagem - 1
        return saiu.valor
    
    

Fila = FilaDeAtendimento()
Pilha = PilhaDeFrascos()
ListaDeVacinados = []



TotalDeFrascos = 3
DosesPorFrasco = 5
MaxDePessoas = 15



for i in range(TotalDeFrascos):   #vai criar 3 elementos fracos com cada um contendo 5 de valor dose
    Pilha.Empilhar(DosesPorFrasco)

DosesTomadas = 0


def TotalDeDosesDisponiveis():
    total = 0
    agora = Pilha.primeiro

    while agora:
        total = total + agora.valor
        agora = agora.proximo

    return total




while True:
    print() #espaçamento
    print("1 - Adicionar pessoa")
    print("2 - Imprimir Pessoas da Fila")
    print("3 - Imprimir quantas doses tem disponíveis")
    print("4 - Vacinar uma pessoa")
    print("5 - Exibir total de pessoas vacinadas")
    print("6 - Encerrar o programa")
    print() #espaçamento

    opcao = input("Escolha uma opção: ")
    print("\n") #espaçamento


    if opcao == "1":
        if Fila.contagem >= MaxDePessoas:  #caso a fila de atendimento ja tiver atingido 15 pessoas
            print("A fila de atendimento ja esta cheia! Numero maximo de 15 pessoas por dia")
        else:
            nome = input("Digite o nome: ")
            cpf = input("Digite o CPF: ")

            pessoa = [nome, cpf]    #lista com 0 e 1 de indice sendo nome e cpf respectivamente
            Fila.Enfileirar(pessoa)
            print(f"{nome} entrou na fila de atendimento!")



    elif opcao == "2":
        if Fila.primeiro is None:
            print("A fila de atendimento esta vazia")
        else:
            Fila.Imprimir()




    elif opcao == "3":
        print(f"Total de doses disponíveis: {TotalDeDosesDisponiveis()}")




    elif opcao == "4":   #vacinar fulano (tirar ele da fila e por na lista de vacinados alem de exibir seus dados)
        if Fila.primeiro is None:
            print("A fila de atendimento esta vazia")

        elif Pilha.primeiro is None:
            print("Acabaram as vacinas!") 

        else:
            pessoa = Fila.Desenfileirar()

            DoseRecemAplicada = Pilha.primeiro.valor
            DoseRecemAplicada = DoseRecemAplicada - 1
            DosesTomadas = DosesTomadas + 1

            ListaDeVacinados.append(pessoa[0])

            print(f"Vacinado!")
            print(f"Nome: {pessoa[0]}") #fazer de pessoa uma lista pra guardar esses dadoszer
            print(f"CPF: {pessoa[1]}")
            print(f"Número da dose aplicada: {DosesPorFrasco - DoseRecemAplicada}º dose")

            if DoseRecemAplicada == 0:  #acabaram as doses do ultimo frasco
                Pilha.Desempilhar()
                print("Acabou mais um frasco de vacinas")
            else:
                Pilha.primeiro.valor = DoseRecemAplicada



    elif opcao == "5":
        print(f"Total de pessoas vacinadas: {len(ListaDeVacinados)}")



    elif opcao == "6":
        break


