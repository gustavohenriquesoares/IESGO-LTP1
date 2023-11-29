class Animal:
    def __init__(self, nome, especie, idade, dieta, habitat):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.dieta = dieta
        self.habitat = habitat

    def descricao(self):
        return f"{self.nome} é um(a) {self.especie} de {self.idade} anos que é {self.dieta}. Habitat: {self.habitat}"

class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)
        print(f"{animal.nome} foi adicionado ao zoológico.")

    def remover_animal(self, nome):
        for animal in self.animais:
            if animal.nome == nome:
                self.animais.remove(animal)
                print(f"{animal.nome} foi removido do zoológico.")
                return
        print(f"Animal com nome {nome} não encontrado no zoológico.")

    def listar_animais(self):
        print("\nLista de Animais no Zoológico:")
        for animal in self.animais:
            print(animal.descricao())

    def buscar_por_especie(self, especie):
        animais_especie = [animal for animal in self.animais if animal.especie == especie]
        if animais_especie:
            print(f"\nAnimais da espécie {especie}:")
            for animal in animais_especie:
                print(animal.descricao())
        else:
            print(f"Nenhum animal da espécie {especie} encontrado no zoológico.")

    def listar_por_habitat(self, habitat):
        animais_habitat = [animal for animal in self.animais if animal.habitat == habitat]
        if animais_habitat:
            print(f"\nAnimais no habitat {habitat}:")
            for animal in animais_habitat:
                print(animal.descricao())
        else:
            print(f"Nenhum animal no habitat {habitat} encontrado no zoológico.")

# Exemplo de uso:
zoo = Zoologico()

leao = Animal("Leo", "Leão", 5, "Carnívoro", "Savana")
pinguim = Animal("Pingu", "Pinguim", 3, "Peixe", "Tundra")
cobra = Animal("Cobra", "Cobra", 2, "Carnívoro", "Floresta Tropical")

zoo.adicionar_animal(leao)
zoo.adicionar_animal(pinguim)
zoo.adicionar_animal(cobra)

zoo.listar_animais()

zoo.buscar_por_especie("Leão")
zoo.listar_por_habitat("Savana")

zoo.remover_animal("Pingu")

zoo.listar_animais()
