def div1(a,b):
    print(a/b)

def div2(func): #decorator
    def inner(a,b):
        if(a<b):
            a,b = b,a
        return func(a,b)
    return inner

div1 = div2(div1)   #calling div1 indirectly
div1(2,4)
