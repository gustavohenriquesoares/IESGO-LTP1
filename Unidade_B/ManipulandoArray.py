# Crie um array de inteiros vazio.
array_inteiros = []

# Peça ao usuário para inserir 5 números inteiros e adicione esses números ao array.
for _ in range(5):
    numero = int(input("Digite um número inteiro: "))
    array_inteiros.append(numero)

# Exiba o array resultante.
print("Array resultante:", array_inteiros)

# Calcule a soma de todos os números no array e exiba o resultado.
soma = sum(array_inteiros)
print("Soma dos números no array:", soma)

# Encontre o valor mínimo e o valor máximo no array e exiba ambos.
minimo = min(array_inteiros)
maximo = max(array_inteiros)
print("Valor mínimo no array:", minimo)
print("Valor máximo no array:", maximo)

# Remova o último elemento do array.
array_inteiros.pop()

# Inverta a ordem dos elementos no array.
array_inteiros.reverse()

# Exiba o array após as operações.
print("Array após as operações:", array_inteiros)
