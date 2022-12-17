# Здесь должен быть твой код
import pandas as pd

df = pd.read_csv('titanic.csv')

df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], inplace=True, axis=1)
df.info()