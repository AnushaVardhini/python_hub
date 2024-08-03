import numpy as np
arr=np.array(24)
print(type(arr),"\n")      #nd array
print(arr.ndim,"\n")       #is has to diplay array name
print ("zero matrix ended\n")


arr1=np.array([1,2,3,4,5,6])
print(type(arr1),"\n")      #nd array
print(arr1.ndim,"\n")       #is has to diplay array name
print ("1d matrix ended\n")

arr2=np.array([[1,2,3,4],[5,6,7,8]])
print(arr2.ndim,"\n")       #is has to diplay array name
print ("2d matrix ended\n")

#3d Matrixs
arr3=np.array([[1,2,3],[5,6,7],[10,11,12]])
print(arr3.ndim,"\n") 
print ("3d matrix ended\n")     

#stroe 2d matrix in the 3d

arr4=np.array([[[1,2,3,4],[5,6,7,8]],[[10,11,12],[13,14,15]]])
print(arr4.ndim,"\n") 
print ("2d  to 3d matrix ended\n")

arr5=np.array([[[1,2,3]]])
print(arr5.ndim,"\n") 

arr6=np.array([1,2,3],ndmin=5)
print(arr5.ndim,"\n")

