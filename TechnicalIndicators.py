from typing import Union
import pandas as pd
import numpy as np
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import datetime
varsymbol = 'VOO'
api_key = 'YOUR-KEY'
x1 = [datetime.date(2010, 11, 13), datetime.date(2021, 7, 15)]
y1 = [95, 370]
x2 = [datetime.date(2010, 11, 13), datetime.date(2021, 7, 15)]
y2 = [18, 270]
ts = TimeSeries(key=api_key, output_format='pandas')
ti = TechIndicators(key=api_key, output_format='pandas')
data_ts, meta_data_ts = ts.get_daily(symbol=varsymbol, outputsize='full')
data_ti, meta_data_ti = ti.get_sma(symbol=varsymbol, time_period=200, series_type='close')
data_rsi, meta_data_rsi = ti.get_rsi(symbol=varsymbol, time_period=70, series_type='close')
data_ema, meta_data_ema = ti.get_ema(symbol=varsymbol, time_period=40, series_type='close')
data_ts.columns = ['open', 'high', 'low', 'close', 'volume']
data_ts = data_ts.sort_index().loc['2008-01-01':]
data_ti = data_ti.loc['2008-01-01':]
data_rsi = data_rsi.loc['2008-01-01':]
data_ema = data_ema.loc['2008-01-01':]
df1 = data_ti
df2 = data_ts['close'].iloc[200 - 1::]
df3 = data_rsi
df4 = data_ema
data_ts.sort_index(inplace=True)
data_ts.head()
total_df = pd.concat([df2, df1, df3, df4], axis=1)
print(total_df)
total_df.plot()
plt.plot(x1, y1, '--', linewidth=3, color='black')
plt.plot(x2, y2, '--', linewidth=3, color='black')
plt.title('TrendLine Stocks Study')
plt.xlabel('Time (Years)')
plt.ylabel('Price')
plt.show()
