# Curso de Scraping
- Lab2 do curso de Scraping da https://www.datascienceacademy.com.br/

## Definição do Problema

Você gosta de correr? Corrida é um dos esportes mais praticados em todo mundo, além de uma atividade saudável e prazerosa.

Neste Lab vamos coletar dados reais de participantes de uma corrida de 10 KM realizada em Hillsboro no Oregon, EUA, em junho de 2017. 

Resumo da corrida:

- Pessoas que completaram a corrida: 577
- Homens: 414
- Mulheres: 163

O objetivo desta análise é encontrar:
    
- O tempo médio de conclusão da corrida.
- Se os tempos de chegada dos corredores seguem uma distribuição normal.
- Analisar se há diferença de desempenho entre homens e mulheres de várias faixas etárias.

Os tempos registrados na corrida (bem como outros dados) são bem precisos pois os participantes usaram sensores RFID de onde os dados foram extraídos e disponibilizados na web. Mais detalhes sobre o uso dos sensores RFID aqui:

https://www.hubertiming.com/runners/faq


## Fonte de Dados

Como fonte de dados usaremos o web site <a href="https://www.hubertiming.com/">Huber Timing</a> que contém o resultado das corridas que acontecem nos EUA, bem como a agenda de novos eventos.

Aqui a página com o resultado da corrida que faremos a análise:

https://www.hubertiming.com/results/2017GPTR10K

## Bibliotecas
- pip install re
- pip install requests
- pip install matplotlib
- pip install numpy
- pip install pandas
- pip install pingouin
- pip install matplotlib
- pip install seaborn
- pip install bs4
- pip install urllib
- pip install scipy
- pip install lxml
