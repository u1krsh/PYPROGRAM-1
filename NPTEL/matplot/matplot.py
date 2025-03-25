import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 
os.chdir("D:/PROGRAM/PYPROGRAM/NPTEL/matplot")

cars = pd.read_csv('Toyota.csv',index_col = 0,na_values=['??','????'])
# plt.scatter(cars['Age'],cars['Price'], c = 'red')
# plt.hist(cars['KM'])
plt.show()