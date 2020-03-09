from numpy import *

arr1 = array([1,3,4,12,9])
arr2 = arr1 #in our memory we still have
#just one array

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2)) #both have same memory location

#=========SOLUTION==========#

arr2 = arr1.view() #shallow copy
print(arr2)
arr1[1]=5
print(arr2)
print(id(arr2))


#shallow copy -> value of 2nd depends upon 1st
#deep copy -> independent values of both arrays

arr2 = arr1.copy() #deep copy
print("Array after copy")
print(arr2)
arr1[1]=69
print("Changed Array 1")
print("Array1= "+str(arr1))
print("Array2= "+str(arr2))
print(id(arr2))