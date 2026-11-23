# Week 8: K-Means, DBSCAN, PCA
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
iris=load_iris(); X=pd.DataFrame(iris.data,columns=iris.feature_names)
Xs=StandardScaler().fit_transform(X)
# K-Means: compare cluster counts
rows=[]
for k in range(2,7):
    km=KMeans(n_clusters=k,n_init=10,random_state=42).fit(Xs)
    rows.append({"k":k,"inertia":km.inertia_,"silhouette":silhouette_score(Xs,km.labels_)})
print(pd.DataFrame(rows).round(3))
# K=3 clusters plotted after dimensional reduction
km=KMeans(n_clusters=3,n_init=10,random_state=42).fit(Xs)
xy=PCA(n_components=2).fit_transform(Xs)
plt.scatter(xy[:,0],xy[:,1],c=km.labels_); plt.title("KMeans clusters projected with PCA"); plt.xlabel("PC1"); plt.ylabel("PC2"); plt.show()
# DBSCAN: try eps values
for eps in [.4,.6,.8,1.0]:
    db=DBSCAN(eps=eps,min_samples=5).fit(Xs)
    print("eps",eps,"labels",np.unique(db.labels_),"noise points",(db.labels_==-1).sum())
# Questions: Compare KMeans and DBSCAN, silhouette, PCA information loss, why scaling matters.