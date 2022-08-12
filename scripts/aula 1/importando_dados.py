#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise, construção e visualização de dados - IDP - 02/2022

Obtendo dados utilizando Python

@author: cafe
"""

## Abrindo arquivos com Python

arquivo = 'Filmes.csv'

## Utilizando o open()
f = open(arquivo)
print(f.read()) 
f = open(arquivo)
print(f.readline()) 

for line in f:
    print(line)
f.close()

## Melhor maneira de usar
with open(arquivo) as f:
    print(f.read()) 
    f = open(arquivo)
    print(f.readline()) 
    
    for line in f:
        print(line)
    
## Utilizando o Pandas

import pandas as pd

arquivo = "Filmes.csv"

# Abrir CSV como DataFrame
dados_filmes = pd.read_csv(arquivo)
# Acessar colunas de um DF
# Executar funções de análise estatística de um DF