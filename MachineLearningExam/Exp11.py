#HEIRARCHICAL CLUSTERING
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

df = pd.read_excel('exp8.xlsx')

X = df.drop(columns=['target'])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
Z = linkage(X_scaled, method='ward')

plt.figure(figsize=(12, 8))
dendrogram(Z)
plt.show()

clusters = fcluster(Z, 2,criterion='maxclust')
df["Cluster"] = clusters
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1],c=clusters, cmap='prism')

plt.xlabel("Feature 1 (mean radius - scaled)")
plt.ylabel("Feature 2 (mean texture -scaled)")
plt.show()
y_true = df["target"]
y_pred = df["Cluster"]
acc1 = accuracy_score(y_true, y_pred-1)
acc2 = accuracy_score(y_true, 2-y_pred)
accuracy = max(acc1, acc2)
print("Cluster Accuracy (compared with target):", round(accuracy*100, 2), "%")
print(df[["Cluster", "target"]].head(10))

