import yfinance as yf
import pandas as pd
import openpyxl
import datetime as dt
from datetime import date
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import seaborn as sns

tickers = ['PBR', 'VALE', 'BBDC']
start_dt = dt.datetime.strptime('01/01/2020', '%d/%m/%Y')
data = yf.download(tickers, start=start_dt, end=None)\
    ['Adj Close']
df = pd.DataFrame(data)
df.index = pd.to_datetime \
    (df.index, format='%Y-%m-%d')\
        .strftime('%d/%m/%Y')

df['Data']=df.index
df['Data'] = pd.to_datetime \
    (df['Data'], format='%d/%m/%Y')

df.dtypes
df.head()

#linha abaixo gera arquivo em excel com a tabela construída, foi comentada para não ficar gerando o arquivo sempre que eu rodo o código completo
#df.to_excel('fechamento_bolsa.xlsx')


#time-series em desenvolvimento
decompose = seasonal_decompose(df)
fig, (ax1,ax2,ax3, ax4) = plt.subplots(4,1, figsize=(12,8))
decompose.observed.plot(ax=ax1)
decompose.trend.plot(ax=ax2)
decompose.seasonal.plot(ax=ax3)
decompose.resid.plot(ax=ax4)
plt.tight_layout()





