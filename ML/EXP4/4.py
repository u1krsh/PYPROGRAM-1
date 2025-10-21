import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
data = pd.read_csv("linear_regression_data.csv")

# Split into X and y
X = data[["Experience (Years)"]]
y = data["Salary (in $1000s)"]

# Split into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Output
print("Mean Squared Error:", mse)
print("R² Score:", r2)
print("Regression Coefficient (slope):", model.coef_[0])
print("Intercept:", model.intercept_)

# Plot
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (in $1000s)")
plt.title("Linear Regression Model")
plt.legend()
plt.grid(True)
plt.show()
