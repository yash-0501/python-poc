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
        for i in range (2,n,1):
            c = a+b
            print(a+b)
            a,b=b,c
        
fib(int(input("Enter number of terms")))