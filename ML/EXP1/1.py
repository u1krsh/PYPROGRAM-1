import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Iris.csv")

# Step 3: Convert to Array and Display
array_data = df.to_numpy()
print("CSV as NumPy Array:\n", array_data)

# Step 4: Display First 5 Rows
print("\nFirst 5 Rows:\n", df.head())

# Step 5: Display Last 3 Columns
print("\nLast 3 Columns:\n", df[df.columns[-3:]])

# Step 6: Display Specific Value [Example: Row 2, Column 1]
row_index = 2
column_index = 1
value = df.iloc[row_index, column_index]
print(f"\nValue at Row {row_index + 1}, Column {column_index + 1}: {value}")

# Step 7: Describe the DataFrame
print("\nDataFrame Description:\n", df.describe())

# Step 8: Replace Missing Values with Mean
df_filled = df.fillna(df.mean(numeric_only=True))
print("\nData After Filling Missing Values:\n", df_filled)

# Step 9: Plot a Graph Between Two Features
feature1 = df.columns[0]
feature2 = df.columns[1]

plt.figure(figsize=(8, 5))
plt.plot(df_filled[feature1], df_filled[feature2], marker='o', linestyle='-')
plt.title(f"Plot Between {feature1} and {feature2}")
plt.xlabel(feature1)
plt.ylabel(feature2)
plt.grid(True)
plt.show()

# Step 10: Display Header (Column Names)
print("\nColumn Headers:\n", df.columns.tolist())

