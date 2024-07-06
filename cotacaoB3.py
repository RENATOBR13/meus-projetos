'''
1 - Baixar o arquivo .csv com as cotações de pelo menos 100 dias de uma ação da Bolsa de Valores.Este arquivo
tem a seguinte estrutura de colunas (cabeçalho): DATA, ABERTURA, FECHAMENTO, VARIAÇÃO, MÍNIMO, MÁXIMO, VOLUME.
2 - Criar uma nova "planilha_resumo.csv", contendo apenas as colunas extraídas (DATA e FECHAMENTO).
3 - Através da "planilha_resumo.csv" realizar as seguinte operações:
    a) Calcular o preço médio
    b) Verificar qual foi o preço máximo e mínimo que o papel alcançou no período e as respectiva datas.
    c) Calcular : se um investidor tivesse adquirido 2000 ações no 10º dia do período,qual seria o valor 
    total dos papeis no 70º dia de investimento ?
    d) Criar um gráfico de linhas que plote os dados do papel ao longo do período.
'''
# Importar as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# Importar o arquivo CSV
#klbn11_df = pd.read_csv('KLBN11.csv')
klbn11_df = pd.read_csv("KLBN11.csv")

# Criar novo dataframe com as colunas de DATA e FECHAMENTO
klbn11_resumo = klbn11_df[['DATA','FECHAMENTO']].copy()
klbn11_resumo.columns = ['Data','Fechamento']

# Substituir as vírgulas por pontos na coluna Fechamento
klbn11_resumo['Fechamento'] = klbn11_resumo['Fechamento'].str.replace(',','.').astype(float)

# Exportar o dataframe para um novo arquivo csv
klbn11_resumo.to_csv('klbn11_resumo.csv',index=False)

########## ANALISE DO PAPEL ##########
# 1. Preço médio dos papéis no período
preco_medio = klbn11_resumo['Fechamento'].mean()
print(f'1. Preço médio das ações: R$ {preco_medio:.2f}')

# 2. Preço máximo e mínimo
preco_maximo = klbn11_resumo['Fechamento'].max()
data_preco_maximo = klbn11_resumo.loc[klbn11_resumo['Fechamento'].idxmax(),'Data']
preco_minimo = klbn11_resumo['Fechamento'].min()
data_preco_minimo = klbn11_resumo.loc[klbn11_resumo['Fechamento'].idxmin(),'Data']

# Mostrar os valores
print(f'2. preço máximo de R$ {preco_maximo:.2f} no dia {data_preco_maximo}')
print(f'2. preço mínimo de R$ {preco_minimo:.2f} no dia {data_preco_minimo}')

# Valor dos papéis no dia 70 e Lucro ou Prejuízo no momento
acoes_adquiridas = 2000
data_aquisicao = klbn11_resumo.iloc[9]['Data']
preco_aquisicao = klbn11_resumo.iloc[9]['Fechamento']

data_venda = klbn11_resumo.iloc[69]['Data']
preco_venda = klbn11_resumo.iloc[69]['Fechamento']

valor_investido = acoes_adquiridas * preco_aquisicao
valor_venda = acoes_adquiridas * preco_venda

lucro_prejuizo = valor_venda - valor_investido

print(f'3. Valor total das ações no dia 70: R$ {valor_venda:.2f}')
print(f'O investidor teve {"lucro" if lucro_prejuizo > 0 else "prejuizo"} de R$ {abs(lucro_prejuizo):.2f}')

# Gráfico de evolução dos preços

# Converter a coluna Data para formato datetime
klbn11_resumo['Data'] = pd.to_datetime(klbn11_resumo['Data'], format="%d/%m/%Y")

# Criar gráfico
plt.figure(figsize=(12,6))
plt.plot(klbn11_resumo['Data'], klbn11_resumo['Fechamento'], label='Fechamento', color='blue')
plt.title('Preço de fechamento da KLABIN11 ao longo do período')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.legend()
plt.grid(True)
plt.show()


