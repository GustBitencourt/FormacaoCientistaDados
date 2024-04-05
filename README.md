# FORMAÇÃO EM PYTHON

## 001 - INTRODUÇÃO

- [001 - INTRODUÇÃO AO PYTHON](./001_INTRO/PYTHON/README.md)
- [001 - INTRODUÇÃO AO R](./001_INTRO/PYTHON/README.md)

## 002 - Limpeza e Tratamento de Dados

- [002 - LIMPEZA E TRATAMENTO DE DADOS](./002_Limpeza_Dados/README.md)

## 003 - Visualização de Dados

- Construção de storytelling para solução de problema
- Mostra Conclusões e Evidencias sobre determinado problema
- Possui os seguintes artefatos:
  - Gráficos estáticos: representação instantânea de um conjunto de dados
  - Dashboards: conjunto de gráficos interativos e exibidos em conjunto
  - Infográfico: Mais ricos visualmente, porém não vinculados diretamente a uma fonte
- Organização de informações partem de:
  - Localização
  - Alfabética
  - Tempo
  - Categoria
  - Hierarquia
- ACCENT, D.A.BURN
  - Percepção (Apprehension)
    - Capacidade de perceber corretamente as relações entre as variáveis
    - O gráfico deve maximizar a apreensão das relações entre as variáveis
  - Clareza (Clarity)
    - Capacidade de distinguir visualmente os elementos
    - Os elementos ou relações importantes devem ter destaque
  - Consistência (Consistency)
    - Capacidade de interpretar um gráfico com base na semelhança com os anteriores
  - Eficiência (Efficiency)
    - Capacidade de demonstrar uma relação de forma simples
    - O gráfico deve ser de fácil interpretação
  - Necessidade (Necessity)
    - O gráfico é de fato necessário?
  - Veracidade (Truthfulness)
    - Capacidade de determinar o valor representado pelos elementos gráficos
    - Os elementos gráficos devem ser posicionados e dimensionados com precisão
- Dicas:
  - Evite gráfico de pizza
  - Evitar gráfico 3D
  - Demonstrar menos de 20 números
  - Variar dados e não design
  - O destaque são sempre os dados
  - Evitar linhas de grade
  - Tentar manter de 3 a 9 Informações por tela
  - Percepção de valores:
    - Atentar-se a escolha do Gráfico para transmitir a informação corretamente
    - Gráficos:
      - Barras
        - Comparação de valores discretos
    - Linhas
      - Dados Contínuos
      - Evolução
      - Séries Temporais, com tempo no eixo horizontal, dimensões no vertical
      - Suporta várias categorias
    - Setores
      - Utilizar com poucas categorias
    - Dispersão
      - Mostrar relação entre variáveis
    - Histograma e Boxplot
      - Distriuição de dados
- Checklist
  - Está usando o elemento gráfico adequado?
  - há excesso de elemntos decorativos?
  - Há mais do que 7 elementos visuais no Dashboard?
  - Dados no contexto correto?
  - Apresentam um excesso de detalhe?
  - Dados de maior importância destacado
  - Excesso de elementos não relacionados a dados?
  - Não transcede dimensões da tela
  - Utiliza medidas eficientes
  - Único assunto no dashboard
  - Informações de maior relevância na área de destaque
  - Existe referências de comparação
  - cores coerentes

## 004 - Estatística

- Ciência que se utiliza das teorias probalísticas para explicar a frequência da ocorrência de eventos
- Principais divisões
  1. Descritiva:
      - Organizar demonstrar e resumir dados
  2. Probabilidade:
      - Analisar situações sujeitas ao acaso
  3. Inferência:
      - Obeter respostas sobre um fenômeno com dados representativos
- Observação x Experimento
  - Observação
    - Estudoo em que os elementos analisados não são afetados(pesquisa)
  - Experimento
    - Condição ou tratamentos são impostas a grupos para avaliar o resultado
- Variaveis
  - Quantitativas - Núméricas
    - Contínua: valores reais, podem assumir qualquer intervalo
    - Discreta: números fixos, inteiros e números de intervalo
  - Qualitativas - Categóricas
    - Nominais: categorias sem hierarquia
    - Ordinais: categorias COM hierarquia
- Estatística não é 100% já que depende de
  - Interpretação
  - Escolha
  - Avaliação

### Análise de Dados Exploratória

- Busca obter informações ocultas sobre os dados, tais como:
  - Variação
  - Anomalias
  - Distribuição
  - Tendência
  - Padrões
  - Relações
- Faz parte do pipeline de qualquer processo de análise de dados

### Amostra

- Parte de uma população, selecionada usando alguma técnica que de chances iguais a todos os elementos da população de serem selecionados
  - População: é o alvo do estudo
  - Amostra: subconjunto da população
  - Censo: pesquisa com toda a população
- Permite tirar conclusões sobre uma população
- Uma amostra feita corretamente deve representar as mesmas características da população de onde foi retirada
- Caso contrário é enviesado
- Enviesamento
  - Ocorre ao substimar ou superestimar o parametro da população
  - Causa:
    - pesquisa de pessoas próximas
    - pesquisa internet
    - sem uso de mecanismo de seleção aleatória
- É possível medir a variação esperada a cada amostra diferente

#### Principais Tipos de Amostra

- Aleatória Simples
  - Determinado número de elementos é retirado da população de maneira aleatória
  - todos os mesmobro da população devem ter as mesmas chances de serem selecioandos para amostra
  - Com reposição
    - retorna a população com as mesmas chances de ser selecionado para amostra
  - Sem reposição
    - É retirado da população a ser selecionado para amostra
- Amostra Estratificada
  - População divididas por extrato (religião, raça, tipo sanguineo)
- Amostra sistematica
  - É escolhido um elemento aleatório a aprtir daí cada N elemento alguém é escolhido

### Medidas da Centralidade e Variabilidade

- Média
  - Soma de sálario de jogadores / núemro de jogadores
- Média Ponderada
  - soma de prova * peso delas / pela soma de seus pesos
- Moda
  - O valor mais frequente
- Mediana
  - Valor do meio ao ordenar os valors de maneira crescente
  - Se o valores forem ímpar é o valor do meio, se forma par é  a Média dos valores centrais
- Variância
  - Mostra a regularidade dos dados, como variam em relação a média
- Desvio padrão
  - Raíz quadrada da variância
  - Quanto maior mais afastado da média
- Amplitude
  - diferença entre maior e menor valor
- Quartis
  - Q1: 25% dos menores valores
  - Q2: 50%
  - Q3: 75% dos maiores valores

### Probabilidade

- P = 1 evento certo
- P = 0 evento ímpossivel
- Conceitos:
  - Experimento: o que está sendo estudado
  - Espaço Amostral: todas as possibilidades de ocorrência do evento
  - Evento: resultados ocorrido
  - Exemplo:
    - Jogar Moeda
    - Cara ou Coroa
    - Resultado Cara
- Evento excludente, não pode ocorrer ao mesmo tempo
- Evento Não Excludente, quando pode ocorrer ao mesmo tempo
- Evento dependente, um tem que ocorrer para que o outro possa acontecer
- Eventos independentes, um não afeta o outro
- Calculo
  - Probabilidade é a ocorrência esperada / número de eventos possiveis
- Pequenas amostras estão sujeitas a variações, não reprodutível, não comparável

### Passeio Aleatório

- Sucessão de etapas aleatórias e independentes
- Usada para estudar os preços de ações
- Não é totalmente aleatório
- Existe uma distribuição de probabilidades
- Em Ações de investimento
  - Duas correntes:
    - Comportamento aleatório, logo impresiviseis
    - Comportamento mantém padrão e tendência ao longo do tempo
- Estocástico x Deterministico
  - Estocástico: dada uma mesma entrada a saída pode variar
  - Deterministico: dada a mesma entrada sempre será a mesma saída

### Distribuição

- Usando principalmente na teoria da probabilidade estuda o comportamento de dados aleatórios
- Distribuição Normal
- Os dados se apresentam simetricamente
- Distribuição Normal Padrão
  - mostra o número de desvios padrões que o valor está acima ou abaixo da média (score Z ou valor Z)
  - Usa-se fórmula para calcular a probabilidade de seu dados com relação a tabela Z

### Teorema Central do limite

- Conforme o tamanho da amostra aumenta, a distribuição das médias amostrais se aproxima cada vez mais da distribuição normal
- Independente como os dados estão distribuidos, suas médias estarão normalmente distribuidas

### Estatística Não Paramétrica

- Quando os dados não estão em conformidade com alguma distribuição 
- Quando não se conhece a distribuição dos dados

