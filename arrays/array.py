#an array contains all the values of samee type
#size of arrays in python is not fixed
from array import *

val = array('i',[5,9,8,4,2])

print(val)
print(val.buffer_info()) #gives size of array (address,size)
val.reverse()
print(val)

newArr = array(val.typecode, (a*a for a in val))
newArr.reverse()
print(newArr)

for a in newArr:
    print(a)

i=0
while i<len(val):
    print(val[i])
    i+=1