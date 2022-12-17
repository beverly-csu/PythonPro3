#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('countries of the world.csv')
df = df.dropna()

def clear_type(country_type):
    country_type = country_type.replace(',', '.')
    return float(country_type)

df['Agriculture'] = df['Agriculture'].apply(clear_type)
df['Industry'] = df['Industry'].apply(clear_type)
df['Service'] = df['Service'].apply(clear_type)

def get_type(row):
    if row['Agriculture'] > row['Industry']:
        if row['Agriculture'] > row['Service']:
            return 'Agriculture'
        else:
            return 'Service'
    else:
        if row['Industry'] > row['Service']:
            return 'Industry'
        else:
            return 'Service'

df['Type of country'] = df.apply(get_type, axis=1)

df['Type of country'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.show()

# print(df[df['Type of country'] == 'Service']['Country'].head(10))
# print(df.pivot_table(values='Service', index='Country'))

print(df[df['Type of country'] == 'Service']['Service'].nlargest(10))
# print(df.iloc[[38, 122, 28, 91, 14]]['Country'])
# df.iloc[[38, 122, 28, 91, 14]]['Country'].plot(kind='bar')
# plt.show()
plt.bar([1, 2, 3, 4, 5], [0.954, 0.927, 0.92, 0.906, 0.9])
plt.xlabel(['Colombia', 'Oman', 'Burma', 'South Korea', 'Barbados'])
plt.show()