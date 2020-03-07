#none- val is assigned null/NoneType
a = None
print(type(a))
#numeric- int float complex bool
num = 2.5
print(type(num)) #float
num = 5
print(type(num)) #int
num = 2 + 3j
print(type(num)) #complex
a = 5.6
num = int(a) #conversion
print(num)
print(type(num))
k= float(num) #conversion
print(type(k))
c= complex(a,k) #conversion
print(c)
b = a<k #bool
c = a>k
print(c) #true
print(b) #false
print(type(b)) 
print(int(True)) #1
print(int(False)) #0

#list
a = [24,234,564,32]
print(type(a))

#tuple
a = (24,234,564,32)
print(type(a))

#set
a = {24,234,564,32}
print(type(a))

#string
str = "Hello World"
print(type(str))
st = 'a'
print(type(st))

#range
range(0,10)
print(list(range(10)))
print(list(range(2,10,2))) #even numbers

#dictionary/mapping
d = {'Yash': 'Mi', 'Pandey': 'Samsung', 'Panbude':'POCO'}
print(type(d))
print(d.keys())
print(d.values())
print(d['Yash'])
print(d.get('Pandey'))

