"""EXERCICIOS PYTHON BASICO - Cap03
"""

# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

dia = input("Que dia da semana é hoje? ") 
dia.lower()  

if (dia == 'sabado') or (dia == 'domingo'):
    print("Hoje é dia de descanso")
else:
    print("Você precisa trabalhar!")

# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

lista1 = ['Maca', 'Pera', 'Uva', 'Morango', 'Banana']
lista2 = ['Maca', 'Pera', 'Uva', 'Banana', 'Abacaxi']

print('Morango' in lista1)
print('Morango' in lista2)

# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista

tupla = (3,5,7,9)
lista_tp = []

for item in tupla:
    lista_tp.append(item*2)
print(lista_tp)

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
for n in range(100, 151, 2):
    print(n, end=", ")
print()

# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela

temperatura = 40

while temperatura > 35:
    print(temperatura)
    temperatura -= 1
    
# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

contador = 0

while contador < 100:
    if contador == 23:
        break
    else:
        print(contador, end=', ')
        contador += 1
print()

# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista

lista3 = list()
var = 4

# minha versao
while var <= 20:
    if var%2==0:
        lista3.append(var)
    var += 1
print(lista3)
    
# correcao/simplificacao
while var <=20:
    lista3.append(i)
    i += 2
print(lista3)

# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = range(5, 45, 2)

# minha versao
lista4 = []
for i in nums:
    lista4.append(i)
print(lista4)

# correcao/simplificacao
print(list(nums))

# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')
    
"""
erro 1: identacao
erro 2: falta os dois pontos no final do if
erro 3: falta os dois pontos no final do else
"""

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a 
# vantagem de existir.” (Machado de Assis)

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir." 

print(frase.count('r'))
