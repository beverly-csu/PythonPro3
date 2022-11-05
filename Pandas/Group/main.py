import pandas as pd

df = pd.read_csv('GoogleApps.csv')

temp = df['Category'].value_counts()
print('Кол-во приложений из категории "BUSINESS":', temp['BUSINESS'])

temp = df['Content Rating'].value_counts()
ratio = temp['Teen'] / temp['Everyone 10+']
print('Cоотношение количества приложений (Teen / Everyone 10+):', round(ratio, 2))

temp = df.groupby(by = 'Type')['Rating'].mean()
print('Средний рейтинг платных приложений:', round(temp['Paid'], 2))
print('Разница рейтинга платных и бесплатных приложений:', round(temp['Paid'] - temp['Free'], 2))

temp = df.groupby(by = 'Category')['Size'].agg(['min', 'max'])
print(temp.loc['COMICS'])