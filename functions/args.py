def modify(x):
    print(id(x))
    x = 8
    print("x =",x)

a=10
print(id(a))
modify(a)
print("a =",a) #prints 10 since PASS BY VAL- 
#x and a takes same address

def update(lst):
    print(id(lst))
    lst[1] = 35
    print("New=", lst)

l = [10,20,30]
print("list=",l)
print(id(l))
update(l)
print("list=",l)