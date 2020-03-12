list = [2,4,5,10,23,44,45]
low = 0
upper = len(list)-1
mid =int((low+upper)/2)
pos = -1
n=10
def binarySearch(list,n):
    if(list[mid]==n):
        globals()['pos']=mid
        return True
    elif(list[mid]<n):
        low=mid+1
    else:
        upper=mid-1
    return False

if(binarySearch(list,n)):
    print("Found at Pos:",pos+1)
else:
    print("Not Found")