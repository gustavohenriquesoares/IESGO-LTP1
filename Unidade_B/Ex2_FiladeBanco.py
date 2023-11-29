class Cliente:
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade

class FilaBanco:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, nome, prioridade):
        cliente = Cliente(nome, prioridade)
        if prioridade:
            self.fila.insert(0, cliente)  # Adiciona à frente da fila se tiver prioridade
        else:
            self.fila.append(cliente)  # Adiciona ao final da fila se não tiver prioridade

    def atender_proximo_cliente(self):
        if self.fila:
            cliente_atendido = self.fila.pop(0)
            print(f"Atendendo o cliente: {cliente_atendido.nome}")
        else:
            print("A fila está vazia. Nenhum cliente para atender.")

    def visualizar_fila(self):
        if self.fila:
            print("\nFila de Banco:")
            for i, cliente in enumerate(self.fila, start=1):
                print(f"{i}. {cliente.nome} (Prioridade: {cliente.prioridade})")
        else:
            print("\nA fila está vazia.")

# Programa principal
fila_banco = FilaBanco()

while True:
    print("\n1. Adicionar cliente à fila")
    print("2. Atender próximo cliente")
    print("3. Visualizar fila")
    print("4. Sair do programa")

    opcao = input("Escolha uma opção (1/2/3/4): ")

    if opcao == '1':
        nome = input("Digite o nome do cliente: ")
        prioridade = input("O cliente tem prioridade por lei? (S para Sim, N para Não): ").upper() == 'S'
        fila_banco.adicionar_cliente(nome, prioridade)

    elif opcao == '2':
        fila_banco.atender_proximo_cliente()

    elif opcao == '3':
        fila_banco.visualizar_fila()

    elif opcao == '4':
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
