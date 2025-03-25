import os
import pandas as pd
import numpy as np
os.chdir("D:/PROGRAM/PYPROGRAM/NPTEL/datahand")
data_csv = pd.read_csv('Iris_data_sample.csv',index_col=0,na_values = ["??","###"])
data_excel = pd.read_excel('Iris_data_sample.xlsx',sheet_name = 'Iris_data')
data_txt = pd.read_table('Iris_data_sample.txt')

print(data_csv.dtypes)

