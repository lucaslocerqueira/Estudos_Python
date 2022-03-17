# -> comentário única linha
"""
Comentátio mútiplas linhas
"""

# Trabalhando com strings
# Indices começam em 0
# Índices: [ 0,   1,   2,   3,   4 ]
#          [ -5, -4,  -3,  -2,  -1 ]
#          ['L', 'u', 'c', 'a', 's']
#          (incluso, excluso]
nome = input("Digite seu nome completo: ")
print(nome[0])

# Slice [começe no 0 : termine um antes do 4] ->  (índice 0 até 3)
print(nome[0], nome[0:4])

# Slice com índice não existente
# print(nome[6])

# Pegando todo o slice
print(nome[:])

# Pegando o último índice
print(nome[-1])

# Do índice 2 até o final
# LUCAS -> 'cas'
print(nome[2:])

# [início:fim:passo]
# LUCAS
# S A C U L
print(nome[::-1])

# Formatação e split
# Split retorna um array com itens separados pelo identificador dado.
# Ex.: nomeCompleto = "Lucas Cerqueira"
# nomeCompleto.split(" ") -> ["Lucas", "Cerqueira"]
# Input -> Lucas Cerqueira
# Output -> "Seu nome é X e seu sobrenome é Y"

print(nome.split(" "))

itens = "Lápis,Caneta,Borracha"
primeiro = itens.split(",")[0]
# ["Lápis", "Caneta", "Borracha"]
print(itens.split(",")[0])

# Formatando saída

print("O primeiro item é " + primeiro)  # "O primeiro item é Lápis"
print("O primeiro item é", primeiro)  # "O primeiro item é Lápis"
print(f"O primeiro item é {primeiro}")  # "O primeiro item é Lápis"
# print(f"O primeiro item é {itens[0]}")

# Desafio: Exibir nome e sobrenome da pessoa
# camelCase
# snake_case


# Estratégia -> "Lucas Lima de Oliveira Cerqueira"
# Ao dar split por espaço -> ["Lucas", "Lima", "de", "Oliveira", "Cerqueira"]
# então o primeiro nome é o primeiro índice do array e os demais são sobrenome
# para cada sobrenome no array, eu vou concatenar num só
# Nome -> Lucas
# Sobrenome -> Lima de Oliveira Cerqueira

nome_completo = input("Digite seu nome completo: ")
nome = nome_completo.split(" ")[0]
sobrenome = nome_completo.split(" ")[1:]  # -> ["Lima"]
print(f"Nome: {nome}\nSobrenome: {sobrenome}")
print(f"Nome: {nome}\nSobrenome: {' '.join(sobrenome)}")
