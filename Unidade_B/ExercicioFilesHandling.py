import json

def adicionar_nome_tipo_sanguineo(lista):
    nome = input("Digite o nome: ")
    tipo_sanguineo = input("Digite o tipo sanguíneo: ")
    lista.append({"nome": nome, "tipo_sanguineo": tipo_sanguineo})
    print(f"{nome} com tipo sanguíneo {tipo_sanguineo} adicionado à lista.")

def visualizar_lista(lista):
    if lista:
        print("\nLista de Nomes e Tipos Sanguíneos:")
        for pessoa in lista:
            print(f"Nome: {pessoa['nome']}, Tipo Sanguíneo: {pessoa['tipo_sanguineo']}")
    else:
        print("\nA lista está vazia.")

def salvar_em_arquivo(lista):
    with open("lista_tipos_sanguineos.txt", "w") as arquivo:
        json.dump(lista, arquivo)
        print("Lista salva no arquivo 'lista_tipos_sanguineos.txt'.")

def carregar_do_arquivo():
    try:
        with open("lista_tipos_sanguineos.txt", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Programa principal
lista_nomes_tipos_sanguineos = carregar_do_arquivo()

while True:
    print("\n1. Adicionar nome e tipo sanguíneo")
    print("2. Visualizar lista")
    print("3. Salvar em arquivo")
    print("4. Sair do programa")

    opcao = input("Escolha uma opção (1/2/3/4): ")

    if opcao == '1':
        adicionar_nome_tipo_sanguineo(lista_nomes_tipos_sanguineos)

    elif opcao == '2':
        visualizar_lista(lista_nomes_tipos_sanguineos)

    elif opcao == '3':
        salvar_em_arquivo(lista_nomes_tipos_sanguineos)

    elif opcao == '4':
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
