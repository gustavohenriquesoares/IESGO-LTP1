class Estudante:
    def __init__(self, nome, idade, nota, id):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.id = id

    def alterar_nota(self, nova_nota):
        self.nota = nova_nota

    def informacoes(self):
        return f"Estudante: {self.nome}, Idade: {self.idade}, Nota: {self.nota}, ID: {self.id}"

class Turma:
    def __init__(self):
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)
        print(f"Estudante '{estudante.nome}' adicionado à turma.")

    def remover_estudante(self, estudante_id):
        for estudante in self.estudantes:
            if estudante.id == estudante_id:
                self.estudantes.remove(estudante)
                print(f"Estudante '{estudante.nome}' removido da turma.")
                return
        print(f"Estudante com ID {estudante_id} não encontrado na turma.")

    def media_da_turma(self):
        if not self.estudantes:
            print("A turma está vazia. Não é possível calcular a média.")
            return None
        total_notas = sum(estudante.nota for estudante in self.estudantes)
        media = total_notas / len(self.estudantes)
        return media

    def melhor_estudante(self):
        if not self.estudantes:
            print("A turma está vazia. Não há melhor estudante.")
            return None
        melhor = max(self.estudantes, key=lambda estudante: estudante.nota)
        return melhor

# Exemplo de uso:
turma = Turma()

estudante1 = Estudante("João", 18, 85, 1)
estudante2 = Estudante("Maria", 17, 92, 2)
estudante3 = Estudante("Carlos", 19, 78, 3)

turma.adicionar_estudante(estudante1)
turma.adicionar_estudante(estudante2)
turma.adicionar_estudante(estudante3)

print("\nInformações da Turma:")
print(f"Média da turma: {turma.media_da_turma()}")
melhor = turma.melhor_estudante()
if melhor:
    print(f"Melhor estudante: {melhor.nome}, Nota: {melhor.nota}")

estudante1.alterar_nota(90)
print("\nApós a alteração da nota do Estudante 1:")
print(f"Informações do Estudante 1: {estudante1.informacoes()}")

turma.remover_estudante(2)

print("\nInformações da Turma após remoção:")
for estudante in turma.estudantes:
    print(estudante.informacoes())
