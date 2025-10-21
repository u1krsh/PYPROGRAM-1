import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# Load Dataset correctly (force CSV-style parsing)
data = pd.read_excel("exp 8 dataset.xlsx", header=0)  # read Excel first
data = data.iloc[:,0].str.split(",", expand=True)     # split single column into multiple
data.columns = ["Feature1","Feature2","Feature3","Target"]  # rename columns

print(data.head())

# Features and Target
X = data.drop('Target', axis=1).astype(float)  # convert features to numeric
y = data['Target']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create Decision Tree Classifier
clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf.fit(X_train, y_train)

# Predictions
y_pred = clf.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Visualize the Tree
plt.figure(figsize=(12,8))
plot_tree(clf, feature_names=X.columns, class_names=[str(c) for c in clf.classes_], filled=True)
plt.show()
