import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
os.chdir("D:/PROGRAM/PYPROGRAM/NPTEL/matplot")

cars = pd.read_csv('Toyota.csv',index_col = 0,na_values=['??','????'])

cars2 = cars.copy()
cars3 = cars2.copy()

# print(cars2.isna().sum())
# missing = cars2[cars2.isna().any(axis=1)]
# print(missing)
print(cars2["Age"].mean())
cars2["Age"].fillna(cars2["Age"].mean())
print(cars2["Age"])