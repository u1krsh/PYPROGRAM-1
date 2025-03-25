import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os 
import matplotlib.pyplot as plt

os.chdir("D:/PROGRAM/PYPROGRAM/NPTEL/casestudy/")

data = pd.read_csv('income.csv')
data2 = data.copy()

#EDA
print(data2.info())

print(data2.isna().sum())#no missing value

summary_num = data2.describe()
print(summary_num)

summary_cate = data2.describe(include = "O")
print(summary_cate)

data2["JobType"].value_counts()
data2["occupation"].value_counts()

print(np.unique(data2["JobType"]))
print(np.unique(data2["occupation"]))

data2 = pd.read_csv('income.csv',na_values = [" ?"])

#data pre processing

print(data2.isnull().sum())

missing = data2[data.isna().any(axis =1)]



data3 = data2.dropna(axis=0)
print(data3.isnull().sum())


data3.columns

gender = pd.crosstab(index = data3["gender"], columns = 'count',normalize= True)
print(gender*100)


gender_salstat = pd.crosstab(index = data3["gender"], columns = data3["SalStat"], margins = True, normalize = 'index')
print(gender_salstat)
# SalStat = sns.countplot(data3["SalStat"])



sns.displot(data3["age"], bins = 10, kde = False)
# plt.show()

# Logistic Reggresiosn

data3["SalStat"] = data3["SalStat"].map({" less than or equal to 50,000":0, " greater than 50,000":1})
print(data3["SalStat"])

new_data = pd.get_dummies(data2,drop_first =True)
columns_list = list(new_data.columns)
# print(columns_list )

features = list(set(columns_list) - set(["SalStat"]))
print(features)
