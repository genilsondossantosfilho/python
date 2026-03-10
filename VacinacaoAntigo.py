# ============================
# CLASSE NÓ (Lista Encadeada)
# ============================

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


# ============================
# LISTA ENCADEADA
# ============================

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def get_tamanho(self):
        return self.tamanho


# ============================
# FILA (derivada da lista)
# ============================

class Fila(ListaEncadeada):
    def __init__(self):
        super().__init__()
        self.fim = None

    def enfileirar(self, dado):
        novo = No(dado)

        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

        self.tamanho += 1

    def desenfileirar(self):
        if self.esta_vazia():
            return None

        removido = self.inicio
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        self.tamanho -= 1
        return removido.dado

    def imprimir(self):
        atual = self.inicio
        while atual:
            pessoa = atual.dado
            print(f"Nome: {pessoa['nome']} | CPF: {pessoa['cpf']}")
            atual = atual.proximo


# ============================
# PILHA (derivada da lista)
# ============================

class Pilha(ListaEncadeada):
    def empilhar(self, dado):
        novo = No(dado)
        novo.proximo = self.inicio
        self.inicio = novo
        self.tamanho += 1

    def desempilhar(self):
        if self.esta_vazia():
            return None

        removido = self.inicio
        self.inicio = self.inicio.proximo
        self.tamanho -= 1
        return removido.dado

    def topo(self):
        if self.esta_vazia():
            return None
        return self.inicio.dado


# ============================
# PROGRAMA PRINCIPAL
# ============================

fila = Fila()
pilha_frascos = Pilha()
vacinados = []

TOTAL_FRASCOS = 3
DOSES_POR_FRASCO = 5
MAX_PESSOAS = 15

# 0 - Empilhar os 3 frascos ao iniciar
for i in range(TOTAL_FRASCOS):
    pilha_frascos.empilhar(DOSES_POR_FRASCO)

doses_aplicadas_total = 0


def doses_disponiveis():
    total = 0
    atual = pilha_frascos.inicio

    while atual:
        total += atual.dado
        atual = atual.proximo

    return total


while True:
    print("\n===== MENU =====")
    print("1 - Adicionar pessoa")
    print("2 - Imprimir Pessoas da Fila")
    print("3 - Imprimir quantas doses tem disponíveis")
    print("4 - Vacinar uma pessoa")
    print("5 - Exibir total de pessoas vacinadas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if fila.get_tamanho() >= MAX_PESSOAS:
            print("Fila cheia! Máximo de 15 pessoas por dia.")
        else:
            nome = input("Digite o nome: ")
            cpf = input("Digite o CPF: ")

            pessoa = {"nome": nome, "cpf": cpf}
            fila.enfileirar(pessoa)
            print("Pessoa adicionada à fila com sucesso!")

    elif opcao == "2":
        if fila.esta_vazia():
            print("Fila vazia.")
        else:
            print("\n--- Pessoas na Fila ---")
            fila.imprimir()

    elif opcao == "3":
        print(f"Doses disponíveis: {doses_disponiveis()}")

    elif opcao == "4":
        if fila.esta_vazia():
            print("Não há pessoas na fila.")
        elif pilha_frascos.esta_vazia():
            print("Não há mais doses disponíveis!")
        else:
            pessoa = fila.desenfileirar()
            vacinados.append(pessoa["nome"])

            # Controle de doses
            dose_atual = pilha_frascos.topo()
            dose_atual -= 1
            doses_aplicadas_total += 1

            print(f"\nPessoa vacinada!")
            print(f"Nome: {pessoa['nome']}")
            print(f"CPF: {pessoa['cpf']}")
            print(f"Número da dose aplicada no dia: {doses_aplicadas_total}")

            if dose_atual == 0:
                pilha_frascos.desempilhar()
                print("Frasco esgotado e removido da pilha.")
            else:
                pilha_frascos.inicio.dado = dose_atual

    elif opcao == "5":
        print(f"Total de pessoas vacinadas: {len(vacinados)}")

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida.")