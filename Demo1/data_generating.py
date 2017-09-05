import numpy as np
import matplotlib.pyplot as plt

K = 2

CENTER1 = [0.2,0.6 ]
VAR1 = [[0.2 ,0],[0 ,0.8]]
SIZE1 = 200

CENTER2 = [2,3]
VAR2 = [[0.6,0],[0,0.1]]
SIZE2 = 600

COLOR = 'black'
FILE_NAME = 'fake_data.dat'

cluster1 = np.random.multivariate_normal(CENTER1,VAR1,SIZE1)
cluster2 = np.random.multivariate_normal(CENTER2,VAR2,SIZE2)


fOut = open(FILE_NAME,"w")
for i in xrange(SIZE1):
    fOut.write("%.5f %.5f\n"%(cluster1[i,0],cluster1[i,1]))
for i in xrange(SIZE2):
    fOut.write("%.5f %.5f\n"%(cluster2[i,0],cluster2[i,1]))
fOut.close()

plt.scatter(cluster1[:,0], cluster1[:,1] ,color = COLOR)
plt.scatter(cluster2[:,0], cluster2[:,1] ,color = COLOR)
plt.show()
