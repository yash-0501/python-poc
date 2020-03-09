from numpy import *

arr1 = array([
    [1,2,3],
    [4,5,6]
])

print(arr1)
print(arr1.ndim) #gives dimension or rank
print(arr1.shape) #no of rows and columns
print(arr1.size) 

# ========== CONVERT 2D to 1D ===========
print("2D to 1D")
arr2 = arr1.flatten()
print(arr2)

# ========== CONVERT 1D to 2D ===========
print("1D to 2D")
arr1 = array([
    [1,2,3,4,5,6],
    [7,8,9,1,2,3]
])
arr2 = arr1.flatten()
arr3 = arr2.reshape(3,4) #rows,columns 
print(arr3)

# ========== CONVERT 1D to 3D ===========
print("1D to 3D")
arr1 = array([
    [1,2,3,4,5,6],
    [7,8,9,1,2,3]
])
arr2 = arr1.flatten()
arr3 = arr2.reshape(2,2,3)  
print(arr3)

