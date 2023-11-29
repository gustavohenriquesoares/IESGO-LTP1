class Restaurante:
    def __init__(self):
        self.itens_menu = {
            "hamburger": 11.50,
            "batata frita": 7.00,
            "refrigerante": 7.50,
            "pizza": 30.00,
            "salada": 4.50
        }
        self.pedidos = {}

    def adicionar_pedido(self, numero_pedido):
        self.pedidos[numero_pedido] = {}

    def adicionar_item_pedido(self, numero_pedido, item, quantidade):
        if numero_pedido in self.pedidos and item in self.itens_menu:
            if item in self.pedidos[numero_pedido]:
                self.pedidos[numero_pedido][item] += quantidade
            else:
                self.pedidos[numero_pedido][item] = quantidade
            print(f"Item '{item}' adicionado ao pedido {numero_pedido}.")
        else:
            print("Número do pedido ou item inválido.")

    def calcular_total_pedido(self, numero_pedido):
        if numero_pedido in self.pedidos:
            total = 0
            for item, quantidade in self.pedidos[numero_pedido].items():
                if item in self.itens_menu:
                    total += self.itens_menu[item] * quantidade
            return total
        else:
            print("Número do pedido inválido.")
            return None

# Exemplo de uso:
restaurante = Restaurante()

restaurante.adicionar_pedido(1)
restaurante.adicionar_item_pedido(1, "hamburger", 2)
restaurante.adicionar_item_pedido(1, "refrigerante", 1)

restaurante.adicionar_pedido(2)
restaurante.adicionar_item_pedido(2, "pizza", 1)
restaurante.adicionar_item_pedido(2, "batata frita", 1)

# Exibindo total do pedido 1
total_pedido_1 = restaurante.calcular_total_pedido(1)
print(f"Total do Pedido 1: R${total_pedido_1:.2f}")

# Exibindo total do pedido 2
total_pedido_2 = restaurante.calcular_total_pedido(2)
print(f"Total do Pedido 2: R${total_pedido_2:.2f}")
