a = 10  #global

def fn():
    a=15 #local
    print("Inside fn a=",a)

fn()
print("Outside fn a=",a) 

def fn2():
    print("Inside fn2 a=",a) #global
fn2()
print("Outside fn2 a=",a)

def fn3():
    global a
    a = 29 #global
    print("Inside fn3 a=",a)
fn3()
print("Outside fn3 a=",a)

def fn4():
    a = 9
    print(id(a))
    x = globals()['a']
    print(id(x))

    globals()['a']=69
    print("In fn4 a=",a)

print("Outside before fn4 a=",a)
fn4()
print("Outside after fn4 a=",a)
print(id(a))