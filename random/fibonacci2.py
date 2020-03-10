def fib(n):
    a=0
    b=1
    if(n==1):
        print(a)
    elif(n<1):
        print("Enter a value greater 0")
    else:
        print(a)
        print(b)
        i=1
        while i>0:
            c = a+b
            if(c>=n):
                i=0
                break
            else:
                print(a+b)
                a,b=b,c
        
fib(int(input("Enter a number")))