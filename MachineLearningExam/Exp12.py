#DBSCAN AND OPTICS

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN, OPTICS
df = pd.read_excel('exp8.xlsx')
X = df.drop(columns = ["target"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
dbscan = DBSCAN(eps=0.5, min_samples=1)
db_cluster = dbscan.fit_predict(X_scaled)
optics = OPTICS(eps=0.5, min_samples=5)
optics_cluster = optics.fit_predict(X_scaled)

plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1],c=db_cluster, cmap='prism')
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1],c=optics_cluster, cmap='prism')
plt.show()
