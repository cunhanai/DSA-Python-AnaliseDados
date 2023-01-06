"""Revisao de funcionalidades do Python para Analise de Dados
    Nivel: Python basico
    Tema: Funcoes

    Objetivo: Relembrar e pensar em Python, nao confundindo mais com o Java

    Aluna: Ana Julia da Cunha
"""

# criando e chamando uma uma funcao
def imprimirHelloWorld():
    print("Hello World")    

imprimirHelloWorld()

# criando e chamando uma funcao com parâmetro
def imprimirNome(nome):
    print('Hello %s' %(nome))

imprimirNome('Ana Júlia')

# variaveis globais
var_global = 10

def multiply(n1, n2):
    var_global = n1 + n2
    print(var_global)

multiply(5, 25)
print(var_global)

# variabeis locais
def multiply2(n1, n2):
    var_local = n1 + n2
    print(var_local)

multiply2(5, 25)
# print(var_local)  # erro de variavel nao definida

# funcoes built-in
print(abs(-344))  # retorna o valor absoluto
print(bool(0))  # retorna um valor booleano

# somando os elementos de uma lista
lista = [23, 23, 34, 45]
print(sum(lista))

# funcoes com numero variavel de argumentos
def printVarInfo(arg1, *argVar):
    # imprimindo o valor do primeiro argumento
    print("O parametro passado foi:", arg1)
    
    # imprimindo o valor do segundo argumento
    for item in argVar:
        print("O parâmetro passado foi:", item)
    return;

printVarInfo(10)
printVarInfo('Chocolate', 'Morango', 'Banana')
