#SVM
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
df = pd.read_csv('exp9.csv')

df = df.drop(['id', 'Unnamed: 32'], axis=1)

le = LabelEncoder()
df['diagnosis'] = le.fit_transform(df['diagnosis'])

X  = df.drop('diagnosis', axis=1)
y = df['diagnosis']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train,X_test,y_train,y_test = train_test_split(X_scaled,y,test_size=0.3, random_state=42)
model = SVC(kernel='rbf',C= 1.0,gamma='scale')
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test,y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()

