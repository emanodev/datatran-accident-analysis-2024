# Análise de Acidentes de Trânsito – DATATRAN 2024

Este projeto realiza uma **análise exploratória de dados (EDA)** utilizando o dataset **DATATRAN 2024**, disponibilizado pela **Polícia Rodoviária Federal (PRF)**.

O objetivo é identificar padrões relacionados à gravidade dos acidentes em rodovias federais brasileiras, considerando fatores como:

* Condições meteorológicas
* Horário do acidente
* Tipo de pista
* Número de mortes

## Objetivo do Projeto

A análise busca responder perguntas como:

* Em quais **horários ocorrem mais mortes** em acidentes?
* Existe relação entre **condição meteorológica e gravidade do acidente**?
* O **tipo de pista influencia na severidade dos acidentes**?
* Qual é a **distribuição de acidentes ao longo do dia**?

## Tecnologias Utilizadas

* Python
* Pandas
* Matplotlib
* Seaborn
* NLTK
* Scikit-learn

## Dataset

O dataset utilizado é o **DATATRAN 2024**, contendo registros de acidentes em rodovias federais brasileiras.

Variáveis analisadas no projeto:

* `condicao_metereologica` – condição climática no momento do acidente
* `classificacao_acidente` – classificação da gravidade do acidente
* `horario` – horário da ocorrência
* `mortos` – número de vítimas fatais
* `tipo_pista` – tipo da pista onde ocorreu o acidente

## Instalação

Instale as dependências do projeto:

```id="p8t1ko"
pip install -r requirements.txt
```

## Execução

Execute o script principal:

```id="du3w61"
python accident_analysis.py
```

O programa irá gerar visualizações que ajudam a entender padrões nos acidentes.

## Visualizações Geradas

O script gera quatro gráficos principais:

1. **Mortes por hora do dia**
2. **Classificação dos acidentes por condição meteorológica**
3. **Gravidade dos acidentes por tipo de pista**
4. **Distribuição dos acidentes por horário**

Essas visualizações ajudam a identificar **fatores de risco e padrões temporais** nos acidentes de trânsito.

## Possíveis Melhorias

Algumas extensões possíveis para o projeto incluem:

* Modelos de **Machine Learning para prever gravidade do acidente**
* Análise **geográfica dos acidentes**
* Criação de **dashboards interativos**
* Aplicação de **NLP em descrições de acidentes**

## Fonte dos Dados

Polícia Rodoviária Federal – DATATRAN
