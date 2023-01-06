"""Revisao de funcionalidades do Python para Analise de Dados
    Nivel: Python basico
    Tema: Tuplas

    Objetivo: Relembrar e pensar em Python, nao confundindo mais com o Java

    Aluna: Ana Julia da Cunha
"""

# Tuplas são imutáveis
# Nao sao frequentes, mas sao usadas quando ha necessidade de imutabilidade

# Criando uma tupla
tupla1 = ('Geografia', 23, 'Elefantes')

# Tuplas nao suportam append ou deletar itens, nada que modifique seus valores

print(tupla1[1])  # Retornar elemento de uma tupla
print(len(tupla1))  # tamanho da tupla
print(tupla1[1:])  # slicing
print(tupla1.index("Elefantes"))  # index do elemento

# "ALTERANDO" TUPLAS

# Criando uma tupla
tupla2 = ('A', 'B', 'C')

# transformando a tupla em uma lista
lista_t2 = list(tupla2)
print(lista_t2)

# alterando valores
lista_t2.append("D")

# converter para tupla novamente
tupla2 = tuple(lista_t2)
print(tupla2)
