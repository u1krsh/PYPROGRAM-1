import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
# Load dataset
data = pd.read_csv('bias_variance_dataset.csv')

# Separate features and labels
X = data[['X']].values
y = data['y_observed'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
degrees = [1, 3, 10]  # Low, Medium, High complexity

plt.figure(figsize=(18, 5))

for i, d in enumerate(degrees):
    # Create polynomial features
    poly = PolynomialFeatures(degree=d)
    X_poly_train = poly.fit_transform(X_train)
    X_poly_test = poly.transform(X_test)

    # Train model
    model = LinearRegression()
    model.fit(X_poly_train, y_train)

    # Predict
    y_train_pred = model.predict(X_poly_train)
    y_test_pred = model.predict(X_poly_test)

    # Visualization
    plt.subplot(1, 3, i + 1)
    plt.scatter(X_train, y_train, color='blue', label='Train Data')
    plt.scatter(X_test, y_test, color='green', label='Test Data')

    X_plot = np.linspace(0, 1, 100).reshape(-1, 1)
    X_plot_poly = poly.transform(X_plot)
    y_plot = model.predict(X_plot_poly)

    plt.plot(X_plot, y_plot, color='red', label=f'Degree {d} Fit')
    plt.title(f'Degree = {d}\nTrain MSE: {mean_squared_error(y_train, y_train_pred):.2f} | Test MSE: {mean_squared_error(y_test, y_test_pred):.2f}')
    plt.legend()
plt.show()

