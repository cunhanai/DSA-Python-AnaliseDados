"""Revisao de funcionalidades do Python para Analise de Dados
    Nivel: Python basico
    Tema: Dicionario

    Objetivo: Relembrar e pensar em Python, nao confundindo mais com o Java

    Aluna: Ana Julia da Cunha
"""

# Dicionarios sao criados com chaves {} e virgulas separando

# Dicionarios sao mapeamentos, uma colecao de objetos que sao armazenados por uma chave
# Com os hash Maps do Java

# Consiste de uma chave e em seguida um valor associado

# COMPARANDO LISTAS E DICIONARIOS

# Lista
estudantes_list = ["Matteo", 24, "Fernanda", 22, "Tamires", 26, "Cristiano", 25]
print(estudantes_list)

# Dicionario
estudantes_dict = {"Matteo":24, "Fernanda":22, "Tamires":26, "Cristiano":25}  # os nomes das pessoas sao as chaves do mapeamento
print(estudantes_dict)

# As chaves do dicionario podem funcionar como indices
print(estudantes_dict["Matteo"])

# Adicionar novo mapeamento
estudantes_dict["Pedro"] = 23
print(estudantes_dict)

# Redefinir idade
estudantes_dict["Pedro"] = 34
print(estudantes_dict["Pedro"])

# Limpar dicionario
estudantes_dict.clear()
print(estudantes_dict)

# Deletar dicionario
del estudantes_dict

# FUNCOES

# Recriando dicionario deletado
estudantes = {"Matteo":24, "Fernanda":22, "Tamires":26, "Cristiano":25}

print(len(estudantes))

# Extrair valores, chaves e itens
print(estudantes.keys())
print(estudantes.values())
print(estudantes.items())

# CONCATENAR DICIONARIOS

# Novo dicionario
estudantes2 = {'Erika':28, 'Maria':27, 'Milton':26}

# Atualizar dicionario anterior
estudantes.update(estudantes2)
print(estudantes)

# DICIONARIO DE LISTAS

# Criando um dicionario de listas
dict = {"key1":1230, "key2":[22,356,664,233,1], "key3":['leite', 'maca', 'banana']}
print(dict)

# Acessando as listas
print(dict["key1"])
print(dict['key3'][0].upper())

# Realizar operacoes
var = dict['key2'][0] - 2
print(var)

# DICIONARIOS ALINHADOS

# Criando dicionario alinhado
dict_alinhado = {'key1':{'key2_alinhada':{'key3_alinhada':'Dict alinhado em Python'}}}
print(dict_alinhado)

# Acessando valor alinhado
print(dict_alinhado['key1']['key2_alinhada']['key3_alinhada'])
