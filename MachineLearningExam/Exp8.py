#DECESION TREE
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier,plot_tree
import matplotlib.pyplot as plt

df = pd.read_csv('exp8.xlxs')

print(df.head())

X = df.drop('Target',axis=1)
y = df['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=42)

model = DecisionTreeClassifier(criterion='entropy',random_state=42)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test,y_pred)
acc = accuracy_score(y_test,y_pred)

plt.figure(figsize = (10,10))
plot_tree(model, feature_names = X.columns, class_names = str(model.classes_),filled=True)
plt.show()