import pandas as pd
import plotly.express as px
from dash import Dash,html,dcc
#Passo 1 - importar a base de dados e visualizar
tabela = pd.read_csv("telecom_users.csv")
print(tabela)

#Passo 2 - Tratamento dos dados
tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela)
#Passo 2.1 - Verificar se o Python esta lendo os dados corretamente e corrigir
print(tabela.info())
#Transformando uma coluna de object para númerico
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"],errors="coerce")
print(tabela.info())

#Passo 2.2 - Corrigir linhas vazias  e colunas COMPLETAMENTE vazias
#No nosso caso aqui como são poucas linhas vazias foi optado por excluir elas.
#colunas COMPLETAMENTE vazias  = excluir
tabela = tabela.dropna(how="all", axis=1)

#Linhas com algum valor vazio = excluir
tabela = tabela.dropna(how="any", axis=0)
print(tabela.info())

#Passo 3 - Analise simples (quantos clientes cancelaram e quantos não)
#aqui vamos contar quantos "nao" e "sim" existe
print(tabela["Churn"].value_counts())
#em percentual
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

#Passo 4 - Análise mais completa  - entender a causa dos cancelmanetos/possiveis soluções
#Aqui usei o modulo plotly.express para montar um grafico e exibir ele
#Criando o gráfico
grafico = px.histogram(tabela, x="TotalGasto")
#Exibindo o gráfico
grafico.show()


