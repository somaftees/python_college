import matplotlib.pyplot as plt 

import numpy as np


y1 = np.array([3,8,2,12])

y2= np.array([6,1,12,20])

plt.plot(y1,'s:r',ms=10,mec='r', mfc='r')
plt.plot(y2,'s:b',ms=10,mec='b', mfc='b')
plt.show()