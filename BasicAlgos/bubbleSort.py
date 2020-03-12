list = [5,3,8,6,7,2]

def sort(list):
    for i in range (len(list)-1):
        for j in range (len(list)-i-1):
            if(list[j]>list[j+1]):
                temp = list[j]
                list[j]=list[j+1]
                list[j+1]=temp


sort(list)
print(list)