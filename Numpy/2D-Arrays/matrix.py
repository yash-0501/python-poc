from numpy import *

arr1 = array([
    [1,2,3],
    [5,6,7],
    [2,4,6]
])

m = matrix(arr1)
print(m)

m2 = matrix('1 2 3 ; 5 5 6 ; 2 5 8 ')
print(m2) #no need of separate array

print(diagonal(m))
print(m.min())
print(m.max())

m3 = m * m2
print(m3)