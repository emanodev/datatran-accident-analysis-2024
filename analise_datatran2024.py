import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega o dataset com delimitador correto e ignora linhas problemáticas
df = pd.read_csv(
    "datatran2024.csv",
    sep=';',
    encoding="latin1",
    on_bad_lines='skip',
    engine='python'
)

# Verifica se todas as colunas necessárias existem no dataset
expected_columns = [
    'condicao_metereologica',
    'classificacao_acidente',
    'horario',
    'mortos',
    'tipo_pista'
]

missing_columns = [col for col in expected_columns if col not in df.columns]

if missing_columns:
    print(f"As seguintes colunas estão ausentes no dataset: {missing_columns}")

else:

    # Relação entre condição meteorológica e gravidade do acidente
    cond_gravidade = pd.crosstab(
        df['condicao_metereologica'],
        df['classificacao_acidente']
    )

    # Extrai a hora do horário do acidente
    df['hora'] = pd.to_datetime(
        df['horario'],
        errors='coerce'
    ).dt.hour

    # Soma de mortes por hora
    hora_gravidade = df.groupby('hora')['mortos'].sum()

    # Relação entre tipo de pista e gravidade
    pista_gravidade = pd.crosstab(
        df['tipo_pista'],
        df['classificacao_acidente']
    )

    # Visualização dos dados
    plt.figure(figsize=(15, 10))

    # Gráfico de mortes por hora
    plt.subplot(2, 2, 1)
    sns.lineplot(
        x=hora_gravidade.index,
        y=hora_gravidade.values,
        marker="o",
        color="red"
    )
    plt.title("Mortes por Hora")
    plt.xlabel("Hora do Dia")
    plt.ylabel("Número de Mortes")
    plt.grid()

    # Classificação de acidentes por condição meteorológica
    plt.subplot(2, 2, 2)
    cond_gravidade.plot(
        kind="bar",
        stacked=True,
        colormap="coolwarm",
        ax=plt.gca()
    )
    plt.title("Classificação de Acidentes por Condição Meteorológica")
    plt.xlabel("Condição Meteorológica")
    plt.ylabel("Quantidade de Acidentes")
    plt.xticks(rotation=45)

    # Gravidade por tipo de pista
    plt.subplot(2, 2, 3)
    pista_gravidade.plot(
        kind="bar",
        stacked=True,
        colormap="viridis",
        ax=plt.gca()
    )
    plt.title("Gravidade por Tipo de Pista")
    plt.xlabel("Tipo de Pista")
    plt.ylabel("Número de Acidentes")
    plt.xticks(rotation=45)

    # Distribuição de acidentes por horário
    plt.subplot(2, 2, 4)
    sns.histplot(
        df['hora'].dropna(),
        bins=24,
        kde=True,
        color="orange"
    )
    plt.title("Distribuição dos Acidentes por Hora")
    plt.xlabel("Hora do Dia")
    plt.ylabel("Frequência")

    plt.tight_layout()
    plt.show()
