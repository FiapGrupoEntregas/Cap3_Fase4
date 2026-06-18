# Classificacao de Graos de Trigo

Projeto desenvolvido para analisar, pre-processar e classificar 210 amostras de graos de trigo de tres variedades distintas: Kama, Rosa e Canadian.

## Participantes

| Nome | Matricula |
|------|-----------|
| Natanael Filho | RM52474 |
| Jonattas Felipe | RM572692 |
| BrunaCamila | RM573402 |


## Introducao do Projeto

O conjunto de dados contem medicoes morfologicas de graos de trigo, incluindo area, perimetro, compacidade, comprimento e largura do nucleo, coeficiente de assimetria e comprimento do sulco do nucleo. O objetivo e construir modelos de classificacao capazes de identificar corretamente a variedade de trigo a partir dessas caracteristicas.

O trabalho e dividido em quatro etapas principais:

1. **Analise e pre-processamento dos dados**: exploracao estatistica, visualizacao da distribuicao das caracteristicas, analise de correlacao, tratamento de valores ausentes e escalonamento.
2. **Modelagem**: treinamento e comparacao de cinco algoritmos de classificacao.
3. **Otimizacao**: ajuste de hiperparametros via Grid Search e Randomized Search.
4. **Interpretacao**: analise dos resultados, matrizes de confusao e importancia das caracteristicas.

## Estrutura de Pastas

```
.
├── main.py                      # Script simples de leitura dos dados
├── seeds_analysis.ipynb         # Notebook completo com analise e modelagem
├── seeds_dataset.txt            # Conjunto de dados original
├── requirements.txt             # Dependencias do projeto
├── pyproject.toml               # Configuracao do ambiente uv
├── uv.lock                      # Lock file do uv
└── README.md                    # Este arquivo
```

## Como Executar

### Usando uv (recomendado)

1. Certifique-se de que o `uv` esta instalado.
2. No diretorio do projeto, execute:

```bash
uv sync
uv run jupyter lab
```

3. Abra o arquivo `seeds_analysis.ipynb` e execute as celulas em ordem.

### Usando requirements.txt

Caso prefira usar `pip` em um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Depois, abra `seeds_analysis.ipynb` e execute as celulas.

### Usando o script simples

Para testar apenas a leitura dos dados:

```bash
uv run main.py
```

## Modelos Utilizados

Foram implementados e comparados os seguintes algoritmos de classificacao:

| Modelo | Descricao |
|--------|-----------|
| K-Nearest Neighbors (KNN) | Classifica com base nos k vizinhos mais proximos. Recebeu dados padronizados. |
| Support Vector Machine (SVM) | Encontra hiperplanos de separacao. Recebeu dados padronizados. |
| Random Forest | Ensemble de arvores de decisao. Treinado com dados originais. |
| Naive Bayes | Classificador probabilistico. Treinado com dados originais. |
| Logistic Regression | Modelo linear. Recebeu dados padronizados. |

A divisao dos dados seguiu a proporcao 70% treinamento e 30% teste, com estratificacao para manter o balanceamento entre as tres variedades.

### O que Fazer e Como Analisar os Graficos

1. **Histogramas**: mostram a distribuicao de cada caracteristica. Use-os para identificar assimetrias, outliers e a necessidade de transformacao.
2. **Boxplots por variedade**: comparam as caracteristicas entre Kama, Rosa e Canadian. Barras fora dos bigodes indicam possiveis outliers.
3. **Matriz de correlacao**: exibe a forca das relacoes lineares entre variaveis. Valores proximos de 1 ou -1 indicam alta correlacao.
4. **Pairplot (graficos de dispersao)**: mostra relacoes entre pares de caracteristicas. Cores diferentes representam as variedades, ajudando a visualizar separabilidade.
5. **Comparacao de modelos (barplot)**: compara o F1-score dos modelos baseline e otimizados. Use para identificar o melhor algoritmo.
6. **Importancia das caracteristicas**: indica quais atributos mais contribuiram para as decisoes do Random Forest.

## Resultados Esperados

Os modelos SVM e Random Forest tendem a apresentar os melhores resultados para este dataset, com F1-scores elevados. A otimizacao de hiperparametros pode melhorar ainda mais o desempenho, embora o ganho seja modesto devido ao tamanho e a qualidade dos dados.
