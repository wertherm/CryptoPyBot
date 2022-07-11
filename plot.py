#https://docs.ccxt.com/en/latest/manual.html

import ccxt
import jsonparse

import numpy as np
import pandas as pd

import mplfinance as fplt

from matplotlib import ticker, dates #Para usar ticker.MaxNLocator(4) e dates.date2num
from datetime import datetime #Para usar datetime.fromtimestamp

exchange = ccxt.binance()
par = 'BTC/USDT'

#Se você parametrizar o 'limit' para trazer somente X registros, serão mostrados apenas os X primeiros candles.
list = exchange.fetch_ohlcv(par, '1d', limit=30)

#print (list) #Util para ver a formatacao dessa saida

#Estrutura o list do json em um array
data = np.array(list)
data = data.transpose() #Sem essa linha, as atribuicoes a 'data' abaixo, ficarao inconsistentes

#Cabeçalho das colunas
data = {"time":data[0], "open":data[1], "high":data[2], "low":data[3], "close":data[4], "volume":data[5]}

#Converte do tipo 'numpy.ndarray' para o tipo 'pandas.core.frame.DataFrame'
data = pd.DataFrame(data)

#A atribuição 'data = pandas.DataFrame(data)', deve ficar acima da linha de abaixo. Pois 'data' deve ser do tipo 'pandas.core.frame.DataFrame' e não 'numpy.ndarray', para ter o tratamento abaixo.
data['time'] = data['time'].apply(lambda x: datetime.fromtimestamp(x/1000.0)) #Necessário para não ocorrer o erro: AttributeError: 'float' object has no attribute 'toordinal'. Pode usar .fromtimestamp ou .utcfromtimestamp o resultado será o mesmo.
data = data.set_index('time') #Troca a coluna de indíce ordinal padrão por time.

#print(data) #Util para ver a formatacao dessa saida

#Estilo de cores do grafico
mc = fplt.make_marketcolors(up='tab:blue', down='tab:red', edge='black', wick={'up':'blue','down':'red'}, volume='lawngreen')
s  = fplt.make_mpf_style(base_mpl_style="ggplot", marketcolors=mc)

fplt.plot(data, type='candle', title=par, ylabel='Preco ($)', volume=True, style=s)