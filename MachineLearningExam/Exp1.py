# simple pandas and matplotlib operations
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Exp1.csv')
print(df)
array_data = df.to_numpy()
print("CSV AS numpy array: ",array_data)

print("First 5 rows: ", df.head(5))

print("Last 3 columns",df.tail(3))

row_index =2
column_index =1
value=df.iloc[row_index,column_index]

print(f"Value at row {row_index+1},Columns{column_index+1}: {value}")
print("Data frame Description: ",df.describe())

df_filled = df.fillna(df.mean(numeric_only=True))
print("Data after Missing filled: ",df_filled)

feature1 = df.columns[1]
feature2 = df.columns[2]

plt.figure(figsize=(8,5))
plt.plot(df_filled[feature1],df_filled[feature2],marker='o',linestyle='-')
plt.title(f"Plot Between {feature1} and {feature2}")
plt.xlabel(feature1)
plt.ylabel(feature2)
plt.grid(True)
plt.show()

