import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic.csv')

df_with_index = pd.read_csv('Titanic.csv', index_col='PassengerId')

df.dropna(inplace=True)

df.info()

df.describe()

plt.hist(df['Age'], color='red')
plt.xlabel('Возраст')
plt.ylabel('Количество')
plt.title('Распределение возраста')
plt.show()

df['Fare'].describe()

column_names = df.columns.tolist()
print(column_names)

df.rename(columns={'Pclass': 'Class'}, inplace=True)

female = df[df['Sex'] == 'female']

Ymale = df[(df['Sex'] == 'male') & (df['Survived'] == 1) & (df['Age'] < 32)]

class_1_or_2 = df[(df['Class'] == 1) | (df['Class'] == 2)]

df['Female'] = (df['Sex'] == 'female').astype(int)


unique_embarked = df['Embarked'].unique()
print(unique_embarked)

grouped_survived = df.groupby('Survived').mean()
print(grouped_survived)

grouped_sex_age = df.groupby('Sex')['Age'].agg(['mean', 'median'])
print(grouped_sex_age)

df.columns = df.columns.str.lower()

df.to_csv('Titanic-new.csv', index=False)
