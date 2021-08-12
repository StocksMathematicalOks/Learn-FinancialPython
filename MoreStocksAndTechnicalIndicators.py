import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
api_key = 'your-key'
varsymbol = 'JPM'
ts = TimeSeries(key=api_key, output_format='pandas')
ti = TechIndicators(key=api_key, output_format='pandas')
data_ts, meta_data_ts = ts.get_daily(symbol=varsymbol, outputsize='full')
data_ts, meta_data_ts = ts.get_daily(symbol=varsymbol, outputsize='full')
period1 = 200
period2 = 70
period3 = 40
data_ti, meta_data_ti = ti.get_sma(symbol=varsymbol, time_period=period1, series_type='close')
data_rsi, meta_data_rsi = ti.get_rsi(symbol=varsymbol, time_period=period2, series_type='close')
data_ema, meta_data_ema = ti.get_ema(symbol=varsymbol, time_period=period3, series_type='close')
data_ts.columns = ['open', 'high', 'low', 'close', 'volume']
data_ts = data_ts.loc['2008-01-01':]
data_ti = data_ti.loc['2008-01-01':]
data_rsi = data_rsi.loc['2008-01-01':]
data_ema = data_ema.loc['2008-01-01':]
df1 = data_ti
df2 = data_ts['close'].iloc[period1 - 1::]
df3 = data_rsi
df4 = data_ema
data_ts.sort_index(inplace=True)
data_ts.head()
total_df = pd.concat([df2, df1, df3, df4], axis=1)
print(total_df)
total_df.plot()
plt.savefig('JPMorganTech.png')
plt.show()






























