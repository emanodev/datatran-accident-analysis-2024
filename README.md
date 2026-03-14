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

Essas informações podem ajudar na compreensão de fatores de risco e no desenvolvimento de políticas de segurança viária.

## Tecnologias Utilizadas

* Python
* Pandas
* Matplotlib
* Seaborn

## Dataset

O dataset utilizado é o **DATATRAN 2024**, contendo registros de acidentes em rodovias federais brasileiras.

Variáveis analisadas no projeto:

* `condicao_metereologica` — condição climática no momento do acidente
* `classificacao_acidente` — classificação da gravidade do acidente
* `horario` — horário da ocorrência
* `mortos` — número de vítimas fatais
* `tipo_pista` — tipo da pista onde ocorreu o acidente

## Instalação

Instale as dependências necessárias:

pip install -r requirements.txt

## Execução

Execute o script principal:

python datatran_accident_analysis.py

O programa irá gerar visualizações que ajudam a identificar padrões nos acidentes.

## Visualizações Geradas

O script produz quatro gráficos principais:

1. **Mortes por hora do dia**
2. **Classificação de acidentes por condição meteorológica**
3. **Gravidade dos acidentes por tipo de pista**
4. **Distribuição de acidentes por horário**

Essas visualizações ajudam a identificar **padrões temporais e fatores de risco** nos acidentes de trânsito.

## Fonte dos Dados

[Polícia Rodoviária Federal – DATATRAN](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf)

## Author

Emanoel Victor  
Data Science Student  
Brazil

