from array import *

arr = array('i',[])

n = int(input("Enter number of values"))

for i in range(n):
    x = int(input("Enter the value"))
    arr.append(x)

print(arr)

num = int(input("Enter the value to search"))
k=0
for e in arr:
    if(e==num):
        print(k)
        break
    k+=1
else:
    print("Not Found")


print(arr.index(num))