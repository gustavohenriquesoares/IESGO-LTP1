import json

def adicionar_nome_tipo_sanguineo(lista, nome, tipo_sanguineo):
    lista[nome] = tipo_sanguineo
    print(f"Nome '{nome}' adicionado com tipo sanguíneo '{tipo_sanguineo}'.")

def visualizar_lista(lista):
    if not lista:
        print("A lista está vazia.")
    else:
        print("Lista de Nomes e Tipos Sanguíneos:")
        for nome, tipo_sanguineo in lista.items():
            print(f"{nome}: {tipo_sanguineo}")

def salvar_em_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(lista, arquivo)
    print(f"Lista salva no arquivo {nome_arquivo}.")

def carregar_de_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

def main():
    nome_arquivo = "lista_tipos_sanguineos.txt"
    lista_tipos_sanguineos = carregar_de_arquivo(nome_arquivo)

    while True:
        print("\nMenu:")
        print("a. Adicionar novo nome e tipo sanguíneo")
        print("b. Visualizar lista atual")
        print("c. Salvar lista em arquivo")
        print("q. Sair")

        opcao = input("Escolha uma opção: ").lower()

        if opcao == 'a':
            nome = input("Digite o nome: ")
            tipo_sanguineo = input("Digite o tipo sanguíneo: ")
            adicionar_nome_tipo_sanguineo(lista_tipos_sanguineos, nome, tipo_sanguineo)

        elif opcao == 'b':
            visualizar_lista(lista_tipos_sanguineos)

        elif opcao == 'c':
            salvar_em_arquivo(lista_tipos_sanguineos, nome_arquivo)

        elif opcao == 'q':
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
