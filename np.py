import numpy as np

arr1 = np.array([30])
arr2 = np.array([1,2,3])
print(arr2[2])
arr3 = np.array([[1,4,5],[3,0,9]])
print(arr3[1,2])
arr4 = np.array([[[1,4,7],[3,12,23]],[[46,9,78],[67,5,9]]])

print(arr4[1,1,1])

print(arr3)
print(arr3.ndim)
print(arr4)
print(arr4.ndim)

print("-----------------------")

print(arr3[0:2,1:3])