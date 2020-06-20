import matplotlib as m
import numpy as np
import pandas as pd
from scipy import stats
import scraping as sc
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg

# Imports para formatação dos gráficos
sns.set_style('whitegrid')

dfScraping = sc.scraping()

# Convertendo a coluna "Chip Time" em apenas minutos
# Chip time é o tempo total de corrida medido com a leitura do sensor RFID no selo da camisa do participante
time_list = dfScraping[' Chip Time'].tolist()

# Visualizando uma amostra de dados
# print(time_list[1:5])

# Lista para receber o resultado da conversão
time_mins = []

# Interação para conversão em minutos
for i in time_list:
    i = i.strip(' ')
    if len(i)!=7:
        i = '0:' + i
    h, m, s = i.split(':')
    math = (int(h) * 3600 + int(m) * 60 + int(s))/60
    time_mins.append(math)

# Nova coluna
dfScraping['Runner_mins'] = time_mins

print(dfScraping.head())

# Cálculo de estatísticas para colunas numéricas no dataframe
print(dfScraping.describe(include = [np.number]))

print('Análise:')
print('- O tempo médio de chip para todos os corredores foi de ~ 60 minutos (a média na tabela acima).')
print('- O corredor 10K mais rápido terminou em 36,35 minutos (valor mínimo na tabela acima).')
print('- O corredor mais lento terminou em 101,30 minutos (valor máximo na tabela acima).')
print(80*'-')

# Vamos criar um boxplot para sumarizar nossa análise.
ax = sns.boxplot(x = dfScraping["Runner_mins"], palette = "Set3", orient = "v")
plt.ylabel('Chip Time')
plt.xlabel('Runners')
plt.show()

# Criaremos agora um gráfico de distribuição dos tempos dos chips dos corredores usando a biblioteca seaborn.
x = dfScraping['Runner_mins']
ax = sns.distplot(x, hist = True, kde = True, rug = False, color = 'blue', bins = 25, hist_kws = {'edgecolor':'black'})
plt.show()

# Separando valor para teste de Normalidade
x = dfScraping['Runner_mins']

# Teste de normalidade com Scipy
print(stats.shapiro(x))

# Teste de normalidade com Pingouin
print(pg.normality(x))

print('Análise:')

print('A variável não segue uma distribuição normal, uma vez que o valor-p é menor que 0.05 e assim há evidências estatísticas para rejeitar a hipótese nula. A função normality() do pacote Pingouin coloca essa informação na última coluna.')
print(80*'-')
print('Vamos agora descobrir se houve alguma diferença de desempenho entre homens e mulheres de várias faixas etárias.')

# Separando os dados de homens e mulheres
f_runners = dfScraping.loc[dfScraping[' Gender'] == ' F']['Runner_mins']
m_runners = dfScraping.loc[dfScraping[' Gender'] == ' M']['Runner_mins']

# Criaremos os 2 plots em uma só figura para facilitar a comparação
sns.distplot(f_runners, hist = True, kde = True, rug = False, hist_kws = {'edgecolor':'black'}, label = 'Mulher')
sns.distplot(m_runners, hist = False, kde = True, rug = False, hist_kws = {'edgecolor':'black'}, label = 'Homem')
plt.legend()
plt.show()

# Análise:

# A distribuição indica que as mulheres eram mais lentas que os homens, em média.

# Computando estatísticas resumidas para homens e mulheres separadamente usando o método groupby ()
g_stats = dfScraping.groupby(" Gender", as_index = True).describe()
print(g_stats)

print('Análise:')

print('O tempo médio de chip para todas as mulheres e homens foi de ~ 66 minutos e ~ 58 minutos, respectivamente, comprovando a análise do gráfico.')

print(80*'-')

print('Um boxplot ajuda a comparar as amostras de homens e mulheres.')

dfScraping.boxplot(column = 'Runner_mins', by = ' Gender')
plt.ylabel('Chip Time')
plt.suptitle("")
plt.show()


