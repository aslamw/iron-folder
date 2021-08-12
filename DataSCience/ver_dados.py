from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt

'''cotacao = web.DataReader('tag', source='site', start='data', end='data')'''
cotacao = web.DataReader('ETH-BTC', data_source='yahoo', start='01-01-2010', end='01-01-2020')
print(cotacao)
cotacao['Adj Close'].plot()
plt.show()
