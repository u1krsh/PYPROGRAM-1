#LDA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

df = load_iris()
X = df.data
y= df.target

ss = StandardScaler()
X_scaled = ss.fit_transform(X)

lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X_scaled, y)

plt.figure(figsize = (8,8))
plt.scatter(X_lda[:, 0], X_lda[:, 1], c = y)
plt.show()