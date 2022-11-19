import pandas as pd

df = pd.read_csv('Space_Corrected.csv')

df.info()
print(df.head(3))

temp = df['Rocket'].dropna()

def cost_to_float(cost):
    cost = cost.replace(',', '')
    return float(cost)

temp = temp.apply(cost_to_float)
median_cost = temp.median()

def fill_rocket(rocket):
    if pd.isnull(rocket):
        return median_cost
    else:
        rocket = rocket.replace(',', '')
        return float(rocket)

# df['Rocket'].fillna(median_cost, inplace=True)
df['Rocket'] = df['Rocket'].apply(fill_rocket)
df.info()