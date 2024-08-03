import numpy as np
arr1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
arr2=np.min(arr1,axis=1)  # row min element in arr1
print(arr2)
arr3=np.max(arr1,axis=1)   # row max element in arr1
print(arr3,"\n")
arr4=np.min(arr1,axis=0)  # Column min element in arr1
print(arr4)
arr5=np.max(arr1,axis=0)   # Columnmax element in arr1
print(arr5)