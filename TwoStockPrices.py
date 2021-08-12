import pandas as pd
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
key = 'YOUR-KEY'
ts = TimeSeries(key, output_format='pandas')
prices, meta = ts.get_daily('MSFT', outputsize='full')
price, meta = ts.get_daily('AAPL', outputsize='full')
prices.columns = ['open', 'high', 'low', 'close', 'volume']
price.columns = ['open', 'high', 'low', 'close', 'volume']
prices.sort_index(inplace=True)
prices.head()
prices = prices.loc['2008-01-01':]
price = price.loc['2008-01-01':]
total_df = pd.concat([prices['close'], price['close']], axis=1)
print(total_df)
total_df.plot()
plt.show()
