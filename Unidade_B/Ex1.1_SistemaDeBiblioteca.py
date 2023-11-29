class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = "disponível"

class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.membros = {}

    def adicionar_livro(self, livro):
        self.livros[livro.titulo] = livro

    def registrar_membro(self, membro):
        self.membros[membro.nome] = membro

    def emprestar_livro(self, titulo_livro, nome_membro):
        if titulo_livro in self.livros:
            livro = self.livros[titulo_livro]
            if livro.status == "disponível":
                if nome_membro in self.membros:
                    membro = self.membros[nome_membro]
                    livro.status = "emprestado"
                    membro.livros_emprestados.append(livro)
                    print(f"{livro.titulo} emprestado para {membro.nome}.")
                else:
                    print("Membro não encontrado.")
            else:
                print("Livro não disponível.")
        else:
            print("Livro não encontrado.")

    def retornar_livro(self, titulo_livro, nome_membro):
        if nome_membro in self.membros:
            membro = self.membros[nome_membro]
            for livro in membro.livros_emprestados:
                if livro.titulo == titulo_livro:
                    livro.status = "disponível"
                    membro.livros_emprestados.remove(livro)
                    print(f"{livro.titulo} retornado por {membro.nome}.")
                    return
            print("Livro não encontrado na lista de empréstimos do membro.")
        else:
            print("Membro não encontrado.")

# Exemplo de uso:
livro1 = Livro("Arte da Guerra", "Sun Tzu")
livro2 = Livro("Jogos Vorazes", "Suzanne Collins")

membro1 = Membro("João")
membro2 = Membro("Maria")

biblioteca = Biblioteca()

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.registrar_membro(membro1)
biblioteca.registrar_membro(membro2)

biblioteca.emprestar_livro("Arte da Guerra", "João")
biblioteca.emprestar_livro("Jogos Vorazes", "Maria")

biblioteca.retornar_livro("Arte da Guerra", "João")

# Exibindo informações
print("\nInformações Atuais:")
for titulo, livro in biblioteca.livros.items():
    print(f"{livro.titulo} ({livro.autor}) - Status: {livro.status}")

for nome, membro in biblioteca.membros.items():
    print(f"{membro.nome} - Livros emprestados: {[livro.titulo for livro in membro.livros_emprestados]}")
