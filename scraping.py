import re
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

def scraping():
    # Definindo a URL com o resultado da corrida
    url = 'https://www.hubertiming.com/results/2017GPTR10K'

    # Abre a conexão com a url
    html = urlopen(url)

    # Extrai o código HTML
    soup = bs(html,'lxml')

    # Extrai o texto do código html
    texto = soup.get_text()

    # Pegando as linhas da tabela
    linhas = soup.find_all('tr')
    # print(linhas[:10])

    # Lista vazia para receber as linhas limpas
    lista_linhas = []

    # Com expressões regulares em Python, vamos extrair os dados das tags HTML.
    for linha in linhas:
        cells = linha.find_all('td')
        str_cells = str(cells)
        clean = re.compile('<.*?>')
        clean2 = (re.sub(clean, '', str_cells))
        clean2 = clean2.replace('\r', '')
        clean2 = clean2.replace('\n', '')
        clean2 = clean2.replace('...', '')
        lista_linhas.append(clean2)

    # Convertemos a lista em dataframe
    df = pd.DataFrame(lista_linhas)

    # Dividindo cada linha e separando os dados a cada vírgula
    df1 = df[0].str.split(',', expand = True)

    # Removemos colchetes de abertura (lado esquerdo) do texto
    df1[0] = df1[0].str.strip('[')

    # Extraímos o cabeçalho de todas as tabelas no código HTML
    col_labels = soup.find_all('th')

    all_header = []
    col_str = str(col_labels)
    cleantext2 = bs(col_str, "lxml").get_text()
    all_header.append(cleantext2)

    # Convertendo a lista de cabeçalhos em um dataframe do pandas
    df2 = pd.DataFrame(all_header)

    # Dividindo a coluna "0" em várias colunas na posição de vírgula para todas as linhas
    df3 = df2[0].str.split(',', expand = True)

    # Concatenando os 2 dataframes
    frames = [df3, df1]
    df4 = pd.concat(frames)

    # Atribuindo a primeira coluna como cabeçalho
    df5 = df4.rename(columns = df4.iloc[0])

    # Removendo todas as linhas com valores ausentes
    df6 = df5.dropna(axis = 0, how = 'any')

    # Descartando o cabeçalho da tabela replicada como a primeira linha no df5
    df7 = df6.drop(df6.index[0])

    # Renomeando as colunas [Place e Team] 
    df7.rename(columns = {'[Place': 'Place'}, inplace = True)
    df7.rename(columns = {' Team]': 'Team'}, inplace = True)

    # Limpeza final dos dados - remoção do colchete de fechamento das células na coluna "Team".
    df7['Team'] = df7['Team'].str.strip(']')
    return df7