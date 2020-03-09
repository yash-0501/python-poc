from numpy import *

arr1 = array([1,3,4,12,9])
arr2 = array([2,5,6,1,8])

arr3 = arr1 + arr2 #adds elements of arr1 + arr2
arr1 = arr1 + 5 #adds 5 to each element
print(arr1)
print(arr3) #vectorized operation

print(sin(arr1)) #sine of each array element
print(cos(arr1)) #cos of each array element
print(log(arr1)) #log of each array element
print(sqrt(arr1)) #sqrt of each array element
print(sum(arr1)) #sum of array elements
print(max(arr1)) #max of array elements
print(min(arr1)) #min of array elements
print(sort(arr1)) #sort an array

print(concatenate([arr1,arr2]))