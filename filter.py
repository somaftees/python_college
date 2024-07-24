import numpy as np

arr = np.array([41,42,43,44])

x=[True,False,True,False]

newarr = arr[x]

print(newarr)

ar = np.array([41,42,43,44])
filter_ar =[]

for a in ar:
    if a > 42:
        filter_ar.append(True)
    else:
        filter_ar.append(False)

newar = ar[filter_ar]
print(newar)

filter_ar=arr>42
newar = ar[filter_ar]
print(newar)


arr2=np.array([1,2,3,4,5,6,7,8,9,10,11,12])

filter_arr2= arr2%2 == 0

newarr2 = arr2[filter_arr2]
print(newarr2)
