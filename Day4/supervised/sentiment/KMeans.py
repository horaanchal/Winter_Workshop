import numpy as np
import pandas as pd

from sklearn.cluster import KMeans

df = pd.read_csv('SrBachchan_tweets.csv')

f1 = df['length'].values
f2 = df['sentiment'].values

X=np.matrix(zip(f1,f2))
print(X)
kmeans=KMeans(n_clusters=4).fit(X)
print(kmeans.labels_)
