import pandas as pd

df = pd.read_csv('GoogleApps.csv')

temp = df.groupby(by = 'Type')['Rating'].agg(['min', 'mean', 'max'])
print(round(temp, 1))

temp = df[df['Type'] == 'Paid'].groupby(by = 'Content Rating')['Size'].agg(['min', 'median', 'max'])
print(round(temp, 1))

temp = df.pivot_table(index='Category', columns='Content Rating', values='Reviews', aggfunc='max')
print(temp)