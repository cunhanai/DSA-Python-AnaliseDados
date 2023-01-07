"""Arquivos

Manipulacao de arquivos.

Para manipulacao de arquivos .txt, podemos utilizar os seguintes metodos:

open()          Usada para abrir um arquivo
read()          Leitura do arquivo
write()         Gravacao do arquivo
seek()          Retorna para o inicio do arquivo
readlines()     Retorna a lista de linhas do arquivo
close()         Fecha o arquivo

Aluna: Ana Julia da Cunha
Python Fundamentos Para Analise de Dados 3.0 - Data Science Academy
"""

# LENDO ARQUIVOS

# abrindo o arquivo para leitura
arq1 = open('cap04/files/file1.txt', 'r')

# lendo o arquivo
print(arq1.read())

# contar o numero de caracteres
print(arq1.tell())

# retornar para o inicio do arquivo
print(arq1.seek(0,0))  # retorna a indexacao

# ler os primeiros 10 caracteres a partir de onde esta o cursor
print(arq1.read(10))

# fechando arquivo
arq1.close()

# GRAVANDO ARQUIVOS

# abrindo arquivo para a escrita/gravacao
arq2 = open('cap04/files/file1.txt', 'w')

# gravando arquivo
arq2.write("Testando gravacao de arquivos em Python")

# fechando arquivo
arq2.close()

# lendo o arquivo gravado
arq2 = open('cap04/files/file1.txt', 'r')
print(arq2.read())

# ACRESCENTANDO CONTEUDO

# abrindo arquivo para fazer o append
arq2 = open('cap04/files/file1.txt', 'a')

# acrescentando conteudo
arq2.write(' Acrescentando conteudo')

# fechando arquivo
arq2.close()

# lendo o arquivo
arq2 = open('cap04/files/file1.txt', 'r')
print(arq2.read())

# retornando ao inicio do arquivo para leitura
arq2.seek(0,0)
print(arq2.read())


# AUTOMATIZANDO O PROCESSO DE GRAVACAO

# definindo o nome do arquivo
fileName = input('Digite o nome do arquivo: ')
fileName = 'cap04/files/' + fileName + '.txt'

# abrindo e escrevendo no arquivo
arq3 = open(fileName, 'w')
arq3.write('Incluindo texto no arquivo criado')
arq3.close()

# lendo o arquivo
arq3 = open(fileName, 'r')
print(arq3.read())
arq3.close()

# ABRINDO UM DATASET EM UMA UNICA LINHA
f = open('cap04/files/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')  # divide o arquivo com base em um criterio
# print(rows)

# CONTANDO AS LINHAS DE UM ARQUIVO
count = 0
for row in rows:
    count += 1
    
print(count)


# DIVIDINDO UM DATASET EM COLUNAS
f = open('cap04/files/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []

for row in rows:
    split_row = row.split((','))
    full_data.append(split_row)
    first_row = full_data[0]  # usada para contar as colunas no proximo item

# print(full_data)

# CONTANDO AS LINHAS DE UM ARQUIVO
count = 0
for row in first_row:
    count += 1
    
print(count)


# OUTROS

arq4 = open('cap04/files/teste2.txt', 'w')
arq4.write('Escrevendo alguma coisa so para ter algo escrito aqui')
arq4.close()

arq4 = open('cap04/files/teste2.txt', 'r')
print(arq4.read())
print(arq4.read())  # nao aparece porque nao ha nada para ser lido, o cursor ja esta no final

# lendo arquivos com o cursor no final
arq4.seek(0)  # definindo cursos pro inicio
print(arq4.readlines())
arq4.close()

# loop for para ler arquivo
for line in open('cap04/files/teste2.txt'):
    print(line)
