import numpy as np

arr = np.array([1,2,1,3,1,5,8,20])
x = np.where(arr == 1)
print(x)

y = np.where(arr%2 == 0)
print(y)

z = np.where(arr == 4)
print(z)


