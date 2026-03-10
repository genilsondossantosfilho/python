# # import Paciente  se usasse assim eu importaria tudo, logo teria q identificar do doc qual classe eu estaria chamando
# # import FilaDeAtendimentoClinico      seria tipo: paciente.paciente("joao")
# from Paciente import Paciente
# from FilaDeAtendimentoClinico import FilaDeAtendimentoClinico


# print("\n")

# # ===================
# # FILA
# # ===================


# # Separar as classes em arquivos externos 
# # primeiro crie as classes e elementos manualmente e depois crie os metodos




# # TESTE COM LISTA ENCADEADA



# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # class FilaDeAtendimentoClinico:
# #     def __init__(self,a1,a2):  #passar o parametro idade e se for > que 60 anos por numa diferente lista
# #         self.first = None     #init é um metodo especial q é  chamado automaticamente toda vez q vc cria um elemento/objeto, passando esses atributos a ele assim q é criado
# #         self.nome = a1   # o atributo nome do objeto vai receber o q for digitado em a1
# #         self.next = a2
# #         # self.idade = a3
    
#     # se deixasse assim toda vez q ela executasse pra criar um objeto ela criaria um novo self.primeiro
# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# # MANUAL

# # class Paciente:
# #     def __init__(self,a1,a2):  #passar o parametro idade e se for > que 60 anos por numa diferente lista
# #         self.nome = a1   # o atributo nome do objeto vai receber o q for digitado em a1
# #         self.next = a2
# #         # self.idade = a3



# # class FilaDeAtendimentoClinico:
# #     def __init__(self):  
# #         self.first = None


# # # I a classe (molde) da fila ja foi criada, falta criar a fila em si

# # # lista = [] assim q se cria uma lista nativa do python q ja vem com metodos prontos (append, pop etc). Use quando precisar de uma lista simples
# # Fila_de_Pacientes = FilaDeAtendimentoClinico()  #estou criando a lista Fila_de_Pacientes e guardando (chamando o metodo) o primeiro objeto da classe FilaDeAtendimentoClinico (q seria o first=None) nela


# # # II Hora de criar os elementos da lista manualmente
# # obj1 = Paciente("Ana Clara",None)
# # obj2 = Paciente("Pedro",None)


# # # III Agora eles foram criados soq estao perdidos no meio da memoria, preciso apontalos uns para os outros
# # Fila_de_Pacientes.first = obj1
# # # obj1 = obj2   isso aqui ta mudando a variavel n ligando os objetos
# # obj1.next = obj2



# # aux = Fila_de_Pacientes.first   #futuro metodo de imprimir fila
# # while aux != None:
# #     print(aux.nome)
# #     aux = aux.next

# #-----------------------------------------------------------------------------------------------------------------------

#    #Automatico



# Fila_de_Pacientes = FilaDeAtendimentoClinico()

# while True:
#     print("\n\n1 - ENTRAR (Inserir nome): \n2 - ATENDER (Primeiro sair da fila): \n3 - MOSTRAR (mostrar quem esta na fila): \n4 - FIM (encerrar):\n")

#     digito = input("Escolha uma opção: ")
#     print("")

#     if digito == "1":
#         pessoa = input("Qual o nome do paciente: ")
#         Fila_de_Pacientes.Entrar(pessoa)

#     elif digito == "2":
#         Fila_de_Pacientes.Atender()

#     elif digito == "3":
#         Fila_de_Pacientes.Mostrar()

#     elif digito == "4":
#         break





# # ------------------------------------------------------------------------------

# # Teste com fila simples

# teria de usar dicionarios se quisesse a idade tbm


# manual

# fila = []

# obj1 = "joao"
# obj2 = "maria"
# fila.append(obj1)
# fila.append(obj2)

# fila.pop(0)


# print(fila)

#-----------------------------------------------------------------------------------------------------------------------

# automatico


# Fila_de_Pacientes = []

# while True:
#     print("\n\n1 - ENTRAR (Inserir nome e idade): \n2 - ATENDER (Primeiro sair da fila): \n3 - MOSTRAR (mostrar quem esta na fila): \n4 - FIM (encerrar):\n")

#     digito = input("Escolha uma opção: ")
#     print("")

#     if digito == "1":
#         nome = input("Qual o nome do paciente: ")
#         idade = input("Quantos anos tem o paciente: ")

#         Fila_de_Pacientes.append({"nome": nome,"idade": idade})


#     elif digito == "2":

#         if not Fila_de_Pacientes:
#             print("N tem ninguem pra atender n")

#         else:
#             print(f"{Fila_de_Pacientes.pop(0)} acabou de ser atendido.")


#     elif digito == "3":
#         a = 0
#         for i in range(len(Fila_de_Pacientes)):
#             print(f'===== Pacientes =====\n\nNome: {Fila_de_Pacientes[a]["nome"]} | Idade: {Fila_de_Pacientes[a]["idade"]}')
#             a += 1

#     elif digito == "4":
#         break 








# # ======================
# # PILHA
# # ======================


# # Teste com pilha simples
# # Teste com pilha encadeada

















# # ======================
# # ARVORES
# # ======================
# print("\n\n\n\n")