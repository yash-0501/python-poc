def add(a,b):  #formal args - position
    c=a+b
    print("Sum =",c)

a,b=5,6
add(a,b) #actual args - position,keyword,default,variable length

def person(name,age=18):#age=18 default
    print(name)
    print(age)

person(age=20,name="Yash")  #keywords

person("Yash") #default age 18 is assigned

def sum(a, *b):  #b is tuple
    c=a
    for i in b:
        c+=i
    print(c)

sum(7,4,3,9) #variable length args