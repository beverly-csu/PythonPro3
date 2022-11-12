import pandas as pd
from data_cleaning import *

# Очистка данных из первого задания

# Замени тип данных на дробное число (float) для цен приложений ('Price')
def set_price(price):
    if price[0] == '$':
        return float(price[1:])
    return 0

df['Price'] = df['Price'].apply(set_price)
# Вычисли, сколько долларов разработчики заработали на каждом платном приложении
def set_installs(installs):
    if installs[-1] == '+':
        installs = installs[:-1]
    installs = installs.replace(',', '')
    return int(installs)

df['Installs'] = df['Installs'].apply(set_installs)

df['Profit'] = df['Installs'] * df['Price']
# Чему равен максимальный доход ('Profit') среди платных приложений (Type == 'Paid')?

# Создай новый столбец, в котором будет храниться количество жанров. Назови его 'Number of genres'

# Какое максимальное количество жанров ('Number of genres') хранится в датасете?

# Бонусное задание
# Создай новый столбец, хранящий сезон, в котором было произведено последнее обновление ('Last Updated') приложения. Назови его 'Season'

# Выведи на экран сезоны и их количество в датасете
