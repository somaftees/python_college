import matplotlib.pyplot as plt 

import numpy as np


x = np.array([2000,2002,2005,2008,2011])

x2= np.array([5,2000,7000,2000,8000])

f1={'color':'purple', 'size':30}
f2={'color':'pink', 'size':30}

plt.plot(x,x2,'s:r',ms=5,mec='r', mfc='r')
plt.title("student",fontdict=f1,loc='left')
plt.xlabel("Year",fontdict=f1)
plt.ylabel("No.stu",fontdict=f2)

plt.show()