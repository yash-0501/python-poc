x = int(input("Enter a Number"))

for i in range (2,x,1):
    if(x%i==0):
        print("Not Prime")
        break
else:
    print("Prime Number "+str(x))