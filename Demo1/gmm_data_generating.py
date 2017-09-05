import numpy as np
import matplotlib.pyplot as plt

K = 2

CENTERS = [[0.2,0.6 ],
           [2,3],
           [3,1.5]]
VARS = [[[0.2 ,0],[0 ,0.8]] ,
        [[0.6,0],[0,0.1]],
        [[0.3,0],[0,0.3]]]
PROPS = [0.2,0.5,1]

N_CLUSTER = len(CENTERS)
SIZE = 1000

MAIN_COLOR = 'black'
COLORS = ['red','blue','yellow','black','green','orange']

FILE_NAME = 'data/fake_data_gmm.dat'

data = np.ndarray((SIZE,K),dtype=float)

list_true_labels = []
for i in xrange(N_CLUSTER):
    list_true_labels.append([])

for i in xrange(SIZE):
    rate = np.random.uniform()
    indx = 0
    for indx in xrange(N_CLUSTER):
        if rate < PROPS[indx]:
            break
    list_true_labels[indx].append(i)
    next_point = np.random.multivariate_normal(CENTERS[indx],VARS[indx],1)
    data[i][0] = next_point[0][0]
    data[i][1] = next_point[0][1]


fOut = open(FILE_NAME,"w")
for i in xrange(SIZE):
    fOut.write("%.5f %.5f\n"%(data[i,0],data[i,1]))
fOut.close()
fig = plt.figure(1)
plt.scatter(data[:,0], data[:,1] ,color = MAIN_COLOR)
fig.savefig("imgs/fake_data.png",format='png', dpi=72)

fig = plt.figure(2)
for i in xrange(N_CLUSTER):
    plt.scatter(data[list_true_labels[i],0],data[list_true_labels[i],1],color=COLORS[i])
plt.savefig("imgs/fake_data_with_labels.png",format='png', dpi=72)
plt.show()

