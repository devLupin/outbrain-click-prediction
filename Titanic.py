"""

Author : Hyuntaek Lim, luckyquit49@gmail.com

Supervisor : Na, In Seop, ypencil@hanmail.net

Starting Project : 2019.1.6

"""

import pandas as pd

train = pd.read_csv('../input/train.csv')
test = pd.read_csv('../input/test.csv')

train.shape
test.shape 
train.info()
test.info()
train.isnull().sum()

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def bar_chart(feature):
    survived = train[train['Survived']==1][feature].value_counts() #count survived people
    dead = train[train['Survived']==0][feature].value_counts() #count dead people
    df = pd.DataFrame([survived,dead]) #데이터프레임으로 묶고
    df.index = ['Survived','Dead'] #add index
    df.plot(kind='bar',stacked=True, figsize=(10,5)) #차트그리기 

bar_chart('Sex')
bar_chart('Pclass')
bar_chart('SibSp')
bar_chart('Embarked')

train.head()
train_test_data = [train, test]
train_test_data

for dataset in train_test_data:
    dataset['Title'] = dataset['Name'].str.extract(' ([A-Za-z]+)\.', expand = False)

train['Title'].value_counts()
test['Title'].value_counts()

title_mapping = {"Mr": 0, "Miss": 1, "Mrs": 2, 
                 "Master": 3, "Dr": 3, "Rev": 3, "Col": 3, "Major": 3, "Mlle": 3,"Countess": 3,
                 "Ms": 3, "Lady": 3, "Jonkheer": 3, "Don": 3, "Dona" : 3, "Mme": 3,"Capt": 3,"Sir": 3 }
for dataset in train_test_data:
    dataset['Title'] = dataset['Title'].map(title_mapping)

train.head()
test.head()

train.drop('Name', axis=1, inplace=True)
test.drop('Name', axis=1, inplace=True)

train.head()
test.head()

bar_chart('Title')

sex_mapping = {"male": 0, "female": 1}
for dataset in train_test_data:
    dataset['Sex'] = dataset['Sex'].map(sex_mapping)

bar_chart('Sex')
train.head(30)

train["Age"].fillna(train.groupby("Title")["Age"].transform("median"), inplace=True)
test["Age"].fillna(test.groupby("Title")["Age"].transform("median"), inplace=True)

train.head(20)

for dataset in train_test_data:
    dataset.loc[ dataset['Age'] <= 16, 'Age'] = 0,
    dataset.loc[(dataset['Age'] > 16) & (dataset['Age'] <= 26), 'Age'] = 1,
    dataset.loc[(dataset['Age'] > 26) & (dataset['Age'] <= 36), 'Age'] = 2,
    dataset.loc[(dataset['Age'] > 36) & (dataset['Age'] <= 62), 'Age'] = 3,
    dataset.loc[ dataset['Age'] > 62, 'Age'] = 4

train.head()
bar_chart('Age')

Pclass1 = train[train['Pclass']==1]['Embarked'].value_counts()
Pclass2 = train[train['Pclass']==2]['Embarked'].value_counts()
Pclass3 = train[train['Pclass']==3]['Embarked'].value_counts()

df = pd.DataFrame([Pclass1, Pclass2, Pclass3])
df.index = ['1st class','2nd class', '3rd class']
df.plot(kind='bar',stacked=True, figsize=(10,5))

for dataset in train_test_data: #fill Nan value with 'S'
    dataset['Embarked'] = dataset['Embarked'].fillna('S')

train.head()

embarked_mapping = {"S": 0, "C": 1, "Q": 2}
for dataset in train_test_data:
    dataset['Embarked'] = dataset['Embarked'].map(embarked_mapping)

train.head()