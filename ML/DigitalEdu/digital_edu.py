import pandas as pd

df = pd.read_csv('train.csv')
df.info()

def debug(name):
    print(df[name].value_counts())

def detect_english(langs):
    langs = langs.split(';')
    if 'English' in langs:
        return 1
    else:
        return 0

df['english'] = df['langs'].apply(detect_english)
