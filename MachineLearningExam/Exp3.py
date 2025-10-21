# bias and variance difference
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import  matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("exp3.csv")

X = data[["X"]].values
y = data["y_observed"].values

X_train, X_test, y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
degress = [1,3,10]

plt.figure(figsize = (18,5))

print(enumerate(degress))
for i,d in enumerate(degress):
    poly = PolynomialFeatures(degree = d)
    X_poly = poly.fit_transform(X_train)
    X_poly_test = poly.transform(X_test)

    model = LinearRegression()
    model.fit(X_poly,y_train)
    y_pred = model.predict(X_poly)
    y_test_pred = model.predict(X_poly_test)

