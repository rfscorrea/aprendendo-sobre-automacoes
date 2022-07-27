import pandas as pd
import plotly.express as px

# tratando base de dados
tabela = pd.read_csv(r'base-de-dados\telecom_users.csv')
tabela = tabela.drop('Unnamed: 0', axis=1)
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

tabela = tabela.dropna(how='all', axis=1)   # excluindo colunas vazias
tabela = tabela.dropna(how='any', axis=0)   # excluindo linhas com alguma informacao vazia

# analisando a base dados
churn_normalized = tabela['Churn'].value_counts(normalize=True)     # quantos cancelaram

# criacao de graficos
for coluna in tabela.columns:
    coluna = coluna
    grafico = px.histogram(tabela, x=coluna, color='Churn' )
    grafico.show()
