import numpy as np

arr1= np.array([12345678910,2,3,4,5,6])
arr2 = np.array(["Hello","python world","arrays"])
print(arr1.dtype)
print(arr2.dtype)

arr3 = np.array([111,2,3,4],dtype='S')
print(arr3)
print(arr3.dtype)


arr4 = np.array([1.1,2.2,3.3,4.4,5.5])
newarr=arr4.astype('i')

print(arr4)
print(arr4.dtype)
print(newarr)
print(newarr.dtype)



arr5 = np.array([1,2,3,4])
narry = arr5.astype('f')

print(arr5)
print(arr5.dtype)
print(narry)
print(narry.dtype)