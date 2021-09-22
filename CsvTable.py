import matplotlib.pyplot as plt
import pandas as pd
data_csv = pd.read_csv('CSV.csv')
data_table = pd.read_csv('Table.csv')
data_csv_keys = data_csv.keys()
data_table_keys = data_table.keys()
time_table = []
value_table = []
empty_array = []
for x in data_table['timestamp']:
    time_table.append(x)
for x in data_table['close (USD)']:
    value_table.append(x)
[float(i) for i in value_table]
'''
for x in range(0, len(value_table)):
    empty_array.append(x)
'''
plt.plot(data_csv['timestamp'], data_csv['close (USD)'], label='Csv Data', color='blue')
plt.plot(time_table, value_table, label='Table Data', color='red')
plt.xlabel('Time')
plt.ylabel('Value ($)')
plt.title('Csv and Tabular Data')
plt.legend()
plt.show()
