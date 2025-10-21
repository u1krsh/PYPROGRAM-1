# bias and variance difference
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import  matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("Ex3.csv")

X = data[["X"]].values
y = data["y_observed"].values

X_train, X_test, y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
degress = [1,3,10]

plt.figure(figsize = (18,5))


for i,d in enumerate(degress):
    poly = PolynomialFeatures(degree = d)
    X_poly = poly.fit_transform(X_train)
    X_poly_test = poly.transform(X_test)

model = LinearRegression()
model.fit(X_poly,y_train)
y_pred = model.predict(X_poly)
y_test_pred = model.predict(X_test)

