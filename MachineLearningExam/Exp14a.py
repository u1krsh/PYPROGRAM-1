# BAGGING
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("exp14.csv")
df = df.dropna()
df = df.drop("Patient Id",axis=1)

target_col = df.columns[-1]

features = df.drop(columns=[target_col]).columns[:int((len(df.columns)-1)/3)]

X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=[target_col]), df[target_col], test_size=0.3, random_state=42)

bag = BaggingClassifier(estimator=DecisionTreeClassifier(max_depth=3), n_estimators=30, random_state=42)
bag.fit(X_train[features], y_train)
y_pred = bag.predict(X_test[features])
print(accuracy_score(y_test, y_pred))