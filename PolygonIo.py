import requests
import matplotlib.pyplot as plt
api_key = 'YOUR_API_KEY'
ticker = 'AAPL'
limit = 100
array = []
time_array = []
time_final = []
debt_array = []
api_url = f'https://api.polygon.io/v2/reference/financials/{ticker}?limit={limit}&apiKey={api_key}'
data = requests.get(api_url).json()
Length = len(data['results'])
for x in range(0, Length):
    time_array.append(data['results'][x]['calendarDate'])
    array.append(data['results'][x]['grossProfit'])
    debt_array.append(data['results'][x]['debtUSD'])
debt_array_final = [int(i) for i in debt_array]
for x in range(0, len(time_array)):
    time_final.append(time_array[x][0:4])
num_time = [int(i) for i in time_final]
plt.plot(num_time, array, label='Gross Profit', color='blue')
plt.plot(num_time, debt_array_final, label='Debt', color='red')
plt.legend()
plt.title('Apple Polygon.io Data')
plt.xlabel('Time (Years)')
plt.ylabel('Value ($)')
plt.show()
