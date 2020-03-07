num = 5
print(id(num))

name="yash"
print(id(name))

a=10
b=a
print(id(a))
print(id(b)) #multiple vars with same data get same address
#makes it memory efficient

print(id(10)) #address is based on the value/object
k=10
print(id(k)) #again same address

a=9
print(id(a))

k=a
print(id(k))

b=8
print(id(b))

print(id(10))#at this point 10 is not being used as val in any var, stored as garbage val 

PI = 3.14
print(type(PI))
print(type('YASH'))
print(type(b))
print(type(a))

