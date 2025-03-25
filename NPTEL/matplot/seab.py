import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
os.chdir("D:/PROGRAM/PYPROGRAM/NPTEL/matplot")

cars = pd.read_csv('Toyota.csv',index_col = 0,na_values=['??','????'])

sns.set_theme(style = 'darkgrid')
# sns.regplot(x = cars['Age'], y = cars['Price'])
# sns.regplot(x = cars['Age'], y = cars['Price'],fit_reg=False)
# sns.lmplot(x = 'Age', y = 'Price',data = cars,fit_reg=False,hue = 'FuelType',legend = True,palette = 'Set2')
# sns.distplot(cars['Age'],kde = False)
# sns.countplot(x  = "FuelType",data = cars)
# sns.countplot (x= "FuelType",data = cars,hue = "Automatic")
sns.boxplot(y=cars["Price"])
plt.show()   