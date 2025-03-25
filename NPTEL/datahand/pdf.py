import os
import pandas as pd
import numpy as np
os.chdir("D:/PROGRAM/PYPROGRAM/NPTEL/datahand")
cars = pd.read_csv("Toyota.csv", index_col=0,na_values = ['???', '????'])
cars['MetColor'] = cars['MetColor'].astype('object')
cars['Automatic'] = cars['Automatic'].astype('object')

print(np.unique(cars['Doors']))
cars['Doors']= cars['Doors'].replace({'three':3})
cars['Doors']=cars['Doors'].replace({'four':4})
cars['Doors']=cars['Doors'].replace({'five':5})
# print(np.unique(cars['Doors']))
