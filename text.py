import matplotlib.pyplot as plt 

import numpy as np


xpoint = np.array([1,2,6,8])

ypoint= np.array([3,8,1,10])

plt.plot(xpoint,ypoint,'o:b',ms=20,mec='r', mfc='r')
plt.show()