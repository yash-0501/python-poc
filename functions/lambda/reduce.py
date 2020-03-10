from functools import *

nums = [3,4,6,1,2,7,9]

even = list(filter(lambda n : n%2==0,nums)) #funcion,sequence
double = list(map(lambda n: n*2,even)) #function,sequence
sum = reduce(lambda a,b:a+b , double) #function,sequence

print(even)
print(double)
print(sum)