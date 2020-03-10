nums = [3,4,6,1,2,7,9]

even = list(filter(lambda n : n%2==0,nums)) #funcion,sequence
double = list(map(lambda n: n*2,even)) #function,sequence

print(even)
print(double)