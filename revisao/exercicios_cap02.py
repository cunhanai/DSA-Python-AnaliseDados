"""EXERCICIOS PYTHON BASICO
"""

# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista1 = [1,2,3,4,5,6,7,8,9,10]
print("Exercicio 1:", lista1)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista2 = ["Ana", "Maio", 18, True, 2]
print("Exercicio 2:", lista2)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
str1 = "Ana"
str2 = "Julia"
str3 = str1 + ' ' + str2
print("Exercicio 3:", str3)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tupla = (1, 2, 2, 3, 4, 4, 4, 5)
print("Exercicio 4:", tupla.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dicionario1 = {}
print("Exercicio 5:", dicionario1)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dicionario2 = {"Ana":18, "Amanda":20, "João":17}
print("Exercicio 6:", dicionario2)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dicionario2["Paula"] = 37
print("Exercicio 7:", dicionario2)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
dicionario3 = {"key_1":12, "key_2":[234, 11], "key_3":"chave"}
print("Exercicio 8:", dicionario3)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
lista3 = ["Ana Julia", (18, 19), {"Programadora":True, "Estudante":False}, 4.5]
print("Exercicio 9:", lista3)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print("Exercicio 10:", frase[0:18])  # da primeira posicao, mas index 0!
