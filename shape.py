import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr1.reshape(4,3)

print(arr1.shape)
print("-----------------")
print(arr1)
print("-----------------")
print(newarr.shape)
print("-----------------")
print(newarr)
print("--------------------------------------------")


arr2=np.array([[1,2,3,4],[5,6,7,8]])
narry = arr2.reshape(-1)
print(arr2)
print("-----------------")
print(arr2.shape)
print("-----------------")
print(narry)
print("--------------------------------------------")


arr3=np.array([1,2,3,4,5,6,7,8,9,10])
narr=np.array_split(arr3,4)
print(arr3)
print("-----------------")
print(narr)
print("--------------------------------------------")