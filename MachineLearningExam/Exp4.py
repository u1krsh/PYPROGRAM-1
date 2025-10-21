#Linear Regression

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

df = pd.read_csv('exp4.csv')

X= df[["Experience (Years)"]]
y = df[["Salary (in $1000s)"]]

X_train, X_test, y_train, y_test = train_test_split(X,y , test_size =0.3, random_state = 42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(mse)
print(r2)
print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)


plt.scatter(X,y,color = 'red')
plt.plot(X,model.predict(X), color = 'blue')

plt.xlabel('Experience (Years)')
plt.ylabel('Salary (in $1000s)')
plt.grid(True)
plt.show()