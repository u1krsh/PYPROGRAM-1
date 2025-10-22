#STACKING
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import StackingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
df = pd.read_csv("exp14.csv")
df = df.dropna()
df = df.drop("Patient Id",axis=1)
target_col = df.columns[-1]

features = df.drop(columns=[target_col]).columns[int(2*(len(df.columns)-1)/3):]

X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=[target_col]),df[target_col], test_size=0.2, random_state=42)

estimators = [('dtc', DecisionTreeClassifier(max_depth=1)),('svc', SVC(probability=True))]

stack = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression())
stack.fit(X_train[features], y_train)
y_pred = stack.predict(X_test[features])
print(accuracy_score(y_test, y_pred))