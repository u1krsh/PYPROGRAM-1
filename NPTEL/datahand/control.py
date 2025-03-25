import os
import pandas as pd
import numpy as np
os.chdir("D:/PROGRAM/PYPROGRAM/NPTEL/datahand")
cars = pd.read_csv("Toyota.csv", index_col=0,na_values = ['???', '????'])

