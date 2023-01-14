import pandas as pd

df = pd.read_csv('/home/idk_ru/Документы/GitHub/PythonPro3/ML/DigitalEdu/train.csv')

def debug(name):
    print(df[name].value_counts())

def detect_english(langs):
    langs = langs.split(';')
    if 'English' in langs:
        return 1
    else:
        return 0


df['english'] = df['langs'].apply(detect_english)

to_drop = [
    'graduation', 'id', 'bdate', 'langs', 'city',
    'life_main', 'people_main', 'last_seen', 'career_start',
    'career_end', 'occupation_name'
]

df['education_form'].fillna('Full-time', inplace=True)
def replace_education_form(education_form):
    if education_form == 'Full-time':
        return 3
    elif education_form == 'Part-time':
        return 2
    else:
        return 1
df['education_form'] = df['education_form'].apply(replace_education_form)

def replace_education_status(education_status):
    if education_status == 'Undergraduate applicant':
        return 1
    elif education_status == "Student (Bachelor's)":
        return 2
    elif education_status == "Student (Specialist)":
        return 3
    elif education_status == "Student (Master's)":
        return 4
    elif education_status == "Alumnus (Bachelor's)":
        return 5
    elif education_status == "Alumnus (Specialist)":
        return 6
    elif education_status == "Alumnus (Master's)":
        return 7
    elif education_status == 'PhD':
        return 8
    elif education_status == "Candidate of Sciences":
        return 9

df['education_status'] = df['education_status'].apply(replace_education_status)

df['occupation_type'].fillna('university', inplace=True)
def replace_occupation_type(occupation_type):
    if occupation_type == 'university':
        return 0
    else:
        return 1
df['occupation_type'] = df['occupation_type'].apply(replace_occupation_type)

df.drop(to_drop, axis=1, inplace=True)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

x = df.drop('result', axis=1)
y = df['result']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
percent = accuracy_score(y_test, y_pred) * 100
print(f"Успешность модели: {round(percent, 2)}%")