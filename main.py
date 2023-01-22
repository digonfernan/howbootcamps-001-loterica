# Objetivo
# O objetivo deste estudo é abordar conceitos de coleta de dados, análisar informações e explorar os resultados.

# Imports
# !pip install lxml
import requests
import pandas as pd
import lxml

# Request da URL
url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotof%C3%A1cil'
# Cria variável de reposta
r = requests.get(url, verify=False)
r # Verifica a resposta
#r.text # Verifica o que foi gravado na variável
r_text = r.text # Cria uma variável nova para facilitar futuras capturas

# Criação do dataframe
df = pd.read_html(r_text) # Grava a variável em um dataframe
type(df) # Verifica o que foi gravado
df[0] # É possível verificar que na linha acima foi gerado uma lista, sendo necessário extrair a informação desejada que está na primeira posição
type (df[0]) # Verifica o que foi gravado
df = df[0].copy # Reescreve o dataframe com a informação necessária
df # Verifica o que foi gravado

# Criação das variáveis conforme constante da Lotofácil
nr_pop = list(range(1, 26)) # Cria a variável de população de 1 a 25 (conforme disponível de acordo com regulamento Lotofácil)
# Criação das listas com números pares, ímpares e primos
nr_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
nr_impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
nr_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23]

# Cria lista de combinação para receber as 25 variáveis possíveis
comb = []
v_01 = 0
v_02 = 0
v_03 = 0
v_04 = 0
v_05 = 0
v_06 = 0
v_07 = 0
v_08 = 0
v_09 = 0
v_10 = 0
v_11 = 0
v_12 = 0
v_13 = 0
v_14 = 0
v_15 = 0
v_16 = 0
v_17 = 0
v_18 = 0
v_19 = 0
v_20 = 0
v_21 = 0
v_22 = 0
v_23 = 0
v_24 = 0
v_25 = 0

# Cria lista de apoio conforme tabela original
lst_campos = ['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5',
'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12',
'Bola13', 'Bola14', 'Bola15']

# Loop para percorrer o dataframe e contar os resultados
for index, row in df.iterrows():
    v_pares = 0
    v_impares = 0
    v_primos = 0
    for campo in lst_campos:
        if row[campo] in nr_pares:
            v_pares += 1
        if row[campo] in nr_impares:
            v_impares += 1
        if row[campo] in nr_primos:
            v_primos += 1
        if row[campo] == 1:
            v_01 += 1
        if row[campo] == 2:
            v_02 += 1
        if row[campo] == 3:
            v_03 += 1
        if row[campo] == 4:
            v_04 += 1
        if row[campo] == 5:
            v_05 += 1
        if row[campo] == 6:
            v_06 += 1
        if row[campo] == 7:
             v_07 += 1
        if row[campo] == 8:
            v_08 += 1
        if row[campo] == 9:
            v_09 += 1
        if row[campo] == 10:
            v_10 += 1
        if row[campo] == 11:
            v_11 += 1
        if row[campo] == 12:
            v_12 += 1
        if row[campo] == 13:
             v_13 += 1
        if row[campo] == 14:
            v_14 += 1
        if row[campo] == 15:
            v_15 += 1
        if row[campo] == 16:
            v_16 += 1
        if row[campo] == 17:
            v_17 += 1
        if row[campo] == 18:
            v_18 += 1
        if row[campo] == 19:
            v_19 += 1
        if row[campo] == 20:
            v_20 += 1
        if row[campo] == 21:
            v_21 += 1
        if row[campo] == 22:
             v_22 += 1
        if row[campo] == 23:
             v_23 += 1
        if row[campo] == 24:
             v_24 += 1
        if row[campo] == 25:
             v_25 += 1
    comb.append(str(v_pares) + 'p-' + str(v_impares) + 'i-'+str(v_primos)+'np')