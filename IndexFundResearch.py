from alpha_vantage.techindicators import TechIndicators
import requests
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
key = 'your-key'
ts = TimeSeries(key, output_format='pandas')
Inflation, meta = ts.get_daily(, outputsize='full')
prices = prices.loc['2008-01-01':]
plt.plot(Inflation)
plt.plot()
#plt.savefig('JPMorgan.png')
plt.show()
