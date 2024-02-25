import pandas as pd

df = pd.read_csv('sw_data.csv')
print(df)
df = pd.read_csv('sw_data.csv',usecols=['hostname', 'location'])
print(df)
df = pd.read_csv('sw_data.csv',usecols=[1, 2])
print(df)