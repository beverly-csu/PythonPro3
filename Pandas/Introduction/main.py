import pandas as pd

df = pd.read_csv('GoogleApps.csv')

print(df.head(1))

print(df.tail(1))

df.info()

print(df.describe())