"""dataset_pandas

Abrindo um dataset com o Pandas

Note que no output ele ja deixa tudo tabelado e bonirinho

Aluna: Ana Julia da Cunha
Python Fundamentos Para Analise de Dados 3.0 - Data Science Academy
"""

import pandas as pd

file_name = 'cap04/files/binary.csv'

df = pd.read_csv(file_name)
print(df.head())

file2 = 'cap04/files/salarios.csv'
df2 = pd.read_csv(file2)
print(df2.head())
