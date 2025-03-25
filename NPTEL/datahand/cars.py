import os
import pandas as pd
import numpy as np
os.chdir("D:/PROGRAM/PYPROGRAM/NPTEL/datahand")
cars = pd.read_csv("Toyota.csv", index_col=0)
# print(cars)

# print(cars.index)
# print(cars.columns)
# print(cars.size)
# print(cars.shape)
# print(cars.memory_usage())
# print(cars.ndim)
# print(cars.head(6))
# print(cars.tail(6))
print(cars.at[4,'FuelType'])
print(cars.loc[:,'FuelType'])
print(cars.dtypes)
print(cars.info())
print(np.unique(cars['KM']))
print(np.unique(cars['HP']))
print(np.unique(cars['MetColor']))