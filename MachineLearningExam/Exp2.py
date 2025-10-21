# confusion matrix using logistic regression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

df = pd.read_csv("exp1.csv")

X = df[['sepal.length','petal.width']]
y= df[['variety']]

X_train,X_test, y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
model = LogisticRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

cm = confusion_matrix(y_test,y_pred)
disp =ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)
disp.plot()
plt.show()