"""Revisao de funcionalidades do Python para Analise de Dados
    Nivel: Python bas ico
    Tema: Expressoes lambda

    Objetivo: Relembrar e pensar em Python, nao confundindo mais com o Java

    Para falar a verdade, nunca vi lambda em Python, apenas em Java 

    Aluna: Ana Julia da Cunha
"""

"""Utilidades do Lambda

- O corpo do lambda é uma única expessao, nao um bloco de instrucoes
- O corpo do lambda é semelhante a uma instrucao de retorno do corpo def
- Criar funções simples

Expressões lamndas sao realmente uteis quando usadas em conjunto com as funcoes
map(), filter() e reduce().

Estrutura:
lambda parametro_de_entrada : retorno_da_funcao

Diferencas:
def -> cria um objeto e atribui um nome a ele (nome da funcao)
lambda -> cria um objeto, mas o retorna como um resultado em tempo de execucao
"""

# processo de simplificacao de funcoes

# 3 linhas de codigo
def potencia(num):
    result = num**2
    return result

print(potencia(5))

# 2 linhas de codigo
def potencia(num):
    return num**2

print(potencia(5))

# 1 linha de codigo
def potencia(num): return num**2

print(potencia(5))

# definindo lambda

# lambda potencia
potencia = lambda num: num**2  # potencia e uma variavel
print(potencia(5))

# lambda de verificacao se é par ou nao
par = lambda x: x%2==0  # resultado booleano
print(par(3))
print(par(4))

# retornar primeiro elemento de uma string

first = lambda s: s[0]
print(first('Python'))

# imprimir o reverso de uma string
reverse = lambda s: s[::-1]
print(reverse('Python'))

# adicionar um numero
addNum = lambda x,y : x+y
print(addNum(2,3))
