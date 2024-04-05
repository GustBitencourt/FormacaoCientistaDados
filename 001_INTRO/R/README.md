# 001 - Introdução ao R

## Packages

- Implementa funções
- Disponiveis nos crambs
- Ex:
  - Intalação: Install.packages("arules", dependencies=TRUE)
  - Carregar: library(arules)
  - Descarregar: detach("package:arules", unload=TRUE)

## Aspectos do R

- getwd() retorna diretório padrão
- setwd("c://caminhodados") transferência de diretório
- retorna classe do objeto: class(obj)
- salva objeto: save(obj, file="arq.ext")
- carrega objeto salvo: load(obj)
- Visualização de dados:
  - plot()
  - hist()
  - boxplot
- R é uma linguagem vetorial, variavel é um vetor de uma única posição

## Tipos de dados

- STring
- Numérico
- Inteiro
- Fator (vetor de texto que pode ser ordenado)

## Atribuindo

- var = 8
- var <- 8L (declarção de valor inteiro)

## Operações

- adição: +
- subtração: "-"
- multiplicação: *
- divisão: /
- potência: "^"
- modo: %%
- divisão de inteiros: %/%

## Operadores lógicos

- maior: >
- maior igual: >=
- igualdade: ==
- diferença: !=
- negação: !
- ou: |
- E: &

## Estrutura de dados

- vetores: x = c(1, 2, 3)
  - leitura x[1]
  - altera posiçao x[1] = 10
- Matrizes
  - linhas e colunas
    - podem ter nomes
  - devem possuir mesmo tipo
  - matriz[linha, coluna]
- Dataframes
  - permite diferentes tipos e dados por coluna
- Lista
  - sequência de ibjetos que podem ser diferentes

## Funções

- Bloco de códigos reutilizaveis
- existem funções já prédefinidas pelo R
- pode criar as suas
