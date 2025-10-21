#KMEANS
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay

df = pd.read_csv('exp8.xlxs')
df = df.drop(['id', 'Unnamed: 32'], axis=1)
le = LabelEncoder()
df['diagnosis'] = le.fit_transform(df['diagnosis'])
X = df.drop(['diagnosis'], axis=1)
y = df['diagnosis']

ss = StandardScaler()
X = ss.fit_transform(X)
model = KMeans(n_clusters=2)
model.fit(X)
cll = model.labels_
if accuracy_score(y,cll )>0.5:
    cll = 1-cll
cm = confusion_matrix(y,cll)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=cll)

disp.plot()
plt.show()