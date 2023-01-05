"""Revisao de funcionalidades do Python para Analise de Dados
    Nivel: Python basico
    Tema: Listas e Matrizes

    Objetivo: Relembrar e pensar em Python, nao confundindo mais com o Java

    Aluna: Ana Julia da Cunha
"""

# LISTAS

# Atribuindo lista
lista1 = [1,2,3,4,5]
print(lista1)

# Deletando item da lista
del lista1[2]
print(lista1)

# LISTAS ALINHADAS (MATRIZES)

# Atribuindo matrizes (note que elas nao precisam ter o mesmo tamanho)
lista2 = [[1,2,3], [4,5,6,7], [8,9,10]]
print(lista2)

# Acessando um item de uma matriz
print(lista2[0][2])

# Concatenação de listas/matrizes
lista3 = lista1 + lista2
print(lista3)

# Operador in
print(100 in lista3)
print(1 in lista3)
print(9 in lista3)
# Perceba que ele nao acessa o numero 9 porque ele esta dentro de outra lista
# Como podemos resolver isso?
print(9 in lista3[6])  # minha solução

# FUNCOES BUILT-IN COM LISTAS

print(len(lista3))  # comprimento da lista
print(max(lista1))  # maior numero da lista
print(min(lista1))  # menor numero da lista

# adicionar item a lista
lista1.append(100)
lista1.append(1)
print(lista1)

print(lista1.count(1))

# extender listas
cidades = ["Florianopolis", "Blumenau", "Joinville"]
cidades.extend(["Itajai", "Camboriu"])
print(cidades)

# acessar index de listas
print(cidades.index("Itajai"))

# inserir um elemento na lista em uma posicao especifica
cidades.insert(3, "Penha")
print(cidades)

# remover elevento da lista pelo valor
cidades.remove("Camboriu")
print(cidades)

# inverter lista
cidades.reverse()
print(cidades)
