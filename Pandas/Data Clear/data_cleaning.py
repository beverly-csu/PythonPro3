import pandas as pd
df = pd.read_csv('GooglePlayStore_wild.csv')
# Выведи информацию о всем DataFrame, чтобы узнать какие столбцы нуждаются в очистке
# Выведи информацию о всем DataFrame, чтобы узнать, какие столбцы нуждаются в очистке
# Сколько в датасете приложений, у которых не указан ('NaN') рейтинг ('Rating')?
temp = df[pd.isnull(df['Rating'])]
print(len(temp))
# Замени пустое значение ('NaN') рейтинга ('Rating') для таких приложений на -1.
df['Rating'].fillna(-1, inplace=True)
# Определи, какое ещё значение размера ('Size') хранится в датасете помимо Килобайтов и Мегабайтов, замени его на -1.
# Преобразуй размеры приложений ('Size') в числовой формат (float). Размер всех приложений должен измеряться в Мегабайтах.
print(df['Size'].value_counts().head(1))

def set_size(size):
    if size[-1] == 'M':
        return float(size[:-1])
    elif size[-1] == 'k':
        return float(size[:-1]) / 1024
    else:
        return -1

df['Size'] = df['Size'].apply(set_size)
# Чему равен максимальный размер ('Size') приложений из категории ('Category') 'TOOLS'?
temp = df[df['Category'] == 'TOOLS']['Size'].max()
print(round(temp, 2))

# Бонусные задания
# Замени тип данных на целочисленный (int) для количества установок ('Installs').
# В записи количества установок ('Installs') знак "+" необходимо игнорировать.
# Т.е. если в датасете количество установок равно 1,000,000+, то необходимо изменить значение на 1000000

# Сгруппируй данные по категории ('Category') и целевой аудитории ('Content Rating') любым удобным для тебя способом,
# посчитай среднее количество установок ('Installs') в каждой группе. Результат округли до десятых.
# В полученной таблице найди ячейку с самым большим значением. 
# К какой возрастной группе и типу приложений относятся данные из этой ячейки?

# У какого приложения не указан тип ('Type')? Какой тип там необходимо записать в зависимости от цены?

# Выведи информацию о всем DataFrame, чтобы убедиться, что очистка прошла успешно