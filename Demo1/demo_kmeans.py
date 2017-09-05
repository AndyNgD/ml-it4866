import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

FILE_NAME = 'data/fake_data_gmm.dat'
COLORS = ['red','blue','yellow','black','green','orange']
N_CLUSTER = 3


data = np.loadtxt(FILE_NAME)

kmeans = KMeans(n_clusters=N_CLUSTER, random_state=0).fit(data)
labels = kmeans.labels_


cluster_labels = []
for i in xrange(N_CLUSTER):
    cluster_labels.append([])

for i in xrange(data.shape[0]):
    label = labels[i]
    cluster_labels[label].append(i)
fig = plt.figure(1)
for i in xrange(N_CLUSTER):
    plt.scatter(data[cluster_labels[i], 0], data[cluster_labels[i], 1], color=COLORS[i])
plt.title("K-Clusters = %s"%N_CLUSTER)
fig.savefig("imgs/demo_result.png")

plt.show()