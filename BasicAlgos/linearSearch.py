pos = -1

def search(list, n):
    i =0 
    while i<len(list):
        if(list[i]==n):
            globals()['pos'] = i
            return True
            break
        i+=1
    return False

list= [10,2,3,43,12,45]

# n=4
n=45

if search(list,n):
    print("Found at: Position",pos+1)
else:
    print("Not Found")