import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

fig = plt.figure()
ax1 = plt.subplot(2,1,1)
ax2 = plt.subplot(2,1,2)

iris = load_iris()
data = np.array(iris['data'])
targets = np.array(iris['target'])

cd = {0:'r',1:'b',2:"g"}
cols = np.array([cd[target] for target in targets])

ax1.scatter(data[:,1], data[:,2], c=cols)#graph 3A
ax2.scatter(data[:,1], data[:,3], c=cols)#graph 3B

plt.show()
